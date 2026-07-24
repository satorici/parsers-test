"""Intentional LOW findings for the bandit parser (issue_severity=LOW)."""


def require_flag(enabled: bool) -> None:
    # B101 — assert used (stripped under -O)
    assert enabled, "flag must be enabled"


def swallow_errors() -> None:
    # B110 — try/except/pass
    try:
        int("not-a-number")
    except Exception:
        pass
