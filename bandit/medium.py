"""Intentional MEDIUM findings for the bandit parser (issue_severity=MEDIUM)."""

import hashlib
import tempfile


def weak_hash(password: str) -> str:
    # B303 / B324 — use of weak MD5 hash
    return hashlib.md5(password.encode()).hexdigest()


def insecure_temp() -> str:
    # B306 — insecure mktemp
    return tempfile.mktemp()
