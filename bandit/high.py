"""Intentional HIGH findings for the bandit parser (issue_severity=HIGH)."""

import pickle
import subprocess


def run_shell(cmd: str) -> None:
    # B602 / B603 — subprocess with shell=True
    subprocess.call(cmd, shell=True)


def load_blob(data: bytes) -> object:
    # B301 — insecure pickle deserialization
    return pickle.loads(data)
