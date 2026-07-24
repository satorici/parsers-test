"""Intentional basedpyright findings: error / warning / information."""

import json  # information — unused import (reportUnusedImport)


def bad_return() -> str:
    # error — return type mismatch (reportReturnType)
    return 42


def unused_warning() -> None:
    # warning — unused variable (reportUnusedVariable)
    leftover = "never read"
    print("ok")
