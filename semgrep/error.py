"""Intentional ERROR finding for the semgrep parser (severity=ERROR, impact=HIGH)."""


def run_user_code(user_input: str) -> None:
    eval(user_input)
