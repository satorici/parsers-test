"""Intentional WARNING finding for the semgrep parser (severity=WARNING, impact=MEDIUM)."""


def require_admin(is_admin: bool) -> None:
    assert is_admin, "admin required"
