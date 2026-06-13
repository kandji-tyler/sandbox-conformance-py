"""Stdlib-only unittest suite (no pytest) — proves the platform-sandbox test
phase genuinely EXECUTES on the bare python-3.13-base image.

Run via repo test_command_override = "python -m unittest -v". The marker rides
back in the result-envelope stdout, proving real execution (not byte-flow).
"""
import unittest

from calc import add, mul

SANDBOX_STDLIB_MARKER = "HYRAX-SANDBOX-STDLIB-CONFORMANCE-OK"


class TestCalcStdlib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_mul(self):
        self.assertEqual(mul(4, 5), 20)

    def test_marker(self):
        print(SANDBOX_STDLIB_MARKER)
        self.assertIn("OK", SANDBOX_STDLIB_MARKER)


if __name__ == "__main__":
    unittest.main()
