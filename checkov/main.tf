# Insecure Terraform for checkov (failed_checks → various severities when annotated).

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "public" {
  bucket = "parsers-tests-public-bucket"
  acl    = "public-read"
}

resource "aws_security_group" "open" {
  name = "parsers-tests-open-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "insecure" {
  identifier           = "parsers-tests-db"
  engine               = "mysql"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  username             = "admin"
  password             = "password123"
  publicly_accessible  = true
  skip_final_snapshot  = true
  storage_encrypted    = false
}
