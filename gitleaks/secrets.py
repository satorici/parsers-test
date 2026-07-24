# Fake secrets for gitleaks (all findings map to HIGH in the frontend parser).
# Synthetic values for parser testing — not real credentials.
# Avoid partner formats that GitHub push protection blocks (Slack xox*, Stripe sk_live_).

github_token = "ghp_abcdefghijklmnopqrstuvwxyz0123456789AB"
gitlab_token = "glpat-abcdefghijklmnopqrst"
npm_token = "npm_abcdefghijklmnopqrstuvwxyz0123456789"
sendgrid_key = "SG.abcdefghijklmnopqrstuv.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrs"

# Minimal PEM-shaped private key block (gitleaks private-key rule)
rsa_private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF6PEXAMPLEKEYMATERIALHERE0001
-----END RSA PRIVATE KEY-----
"""
