// Intentional gosec findings across severities for the dedicated parser.
package main

import (
	"crypto/md5"
	"crypto/tls"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
)

func main() {
	// G101 HIGH — potential hardcoded credentials
	password := "SuperSecretPassword123!"
	fmt.Println(password)

	// G402 HIGH — TLS InsecureSkipVerify
	_ = &tls.Config{InsecureSkipVerify: true}

	// G304 MEDIUM — file inclusion via variable
	path := os.Args[1]
	data, _ := os.ReadFile(path)
	fmt.Println(string(data))

	// G204 MEDIUM — subprocess with variable
	cmd := os.Args[2]
	_ = exec.Command(cmd).Run()

	// Weak hash (md5)
	h := md5.New()
	_, _ = io.WriteString(h, "data")
	fmt.Printf("%x\n", h.Sum(nil))

	_, _ = http.Get("http://example.com/")
}
