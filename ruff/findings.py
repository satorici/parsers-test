"""Intentional Ruff findings across severity-mapped rule prefixes."""

import sys
import os  # I001 — import block should be sorted (INFO)
import json  # F401 — unused import (MEDIUM)

password = "hunter2"  # S105 — hard-coded password string (HIGH)


def use_imports() -> str:
    return f"{os.name}-{sys.platform}"


def unused_assert(flag: bool) -> None:
    assert flag  # S101 — assert used (HIGH)


def trailing():  
    x=1+2  # E225 — missing whitespace (MEDIUM); trailing whitespace above (W291, LOW)
    return x
