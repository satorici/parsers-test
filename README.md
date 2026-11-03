# parsers-test

Fixture playbook for Satori frontend **structured-output** parsers. It runs security tools with JSON/JSONL so report stdout can be checked end-to-end in the Satori web UI. Each tool scans its own fixture folder with intentional findings across severities.

## Run

```bash
satori run ./ --report --output
```

Install and run steps live in [`.satori.yml`](.satori.yml) (Python image; tools via apt, pip, and GitHub release binaries). See [Satori docs](https://docs.satori.ci).

## Tools and fixtures

| Tool | Fixture | Role |
|------|---------|------|
| semgrep | `semgrep/` | Dedicated parser |
| bandit | `bandit/` | Dedicated parser |
| gosec | `gosec/` | Dedicated parser |
| eslint | `eslint/` | Dedicated parser |
| trufflehog | `trufflehog/` | Dedicated parser |
| nuclei | `nuclei/` | Dedicated parser |
| gitleaks | `gitleaks/` | Dedicated parser |
| ruff | `ruff/` | Dedicated parser |
| basedpyright | `basedpyright/` | Dedicated parser |
| trivy | `trivy/` | Dedicated parser |
| checkov | `checkov/` | Dedicated parser |
| pyspector | `pyspector/` | Dedicated parser |
| jsspector | `jsspector/` | Satori JSON fields (dynamic until dedicated) |
| shellcheck | `shellcheck/` | Dynamic fallback parser |

JSON/JSONL flags match the findings-lambda parsers. Exercise them via Satori web UI reports after a run.

## Disclaimer

Secrets, vulnerable packages, and insecure IaC under the fixture directories are **synthetic, intentional test data** — not real credentials or production assets.
