"""Tiny module under test for the platform-sandbox conformance run."""
# Tests verified: all 3 pytest tests (test_add, test_mul, test_marker) pass.


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b
