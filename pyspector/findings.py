"""Intentional pyspector findings across Critical / High / Medium / Low."""

import hashlib
import pickle
import tempfile

import yaml


def critical_exec(code: str) -> None:
    # PY305 — Critical
    exec(code)


def high_eval(expr: str) -> object:
    # PY001 — High
    return eval(expr)


def high_pickle(blob: bytes) -> object:
    # PY002 — High
    return pickle.loads(blob)


def medium_md5(data: str) -> bytes:
    # PY201 — Medium
    return hashlib.md5(data.encode()).digest()


def medium_mktemp() -> str:
    # PY304 — Medium
    return tempfile.mktemp()


def low_pynacl() -> None:
    # PY205 — Low
    import nacl.low_level  # noqa: F401


def critical_yaml(raw: str) -> object:
    # YAML001 — Critical
    return yaml.load(raw)
