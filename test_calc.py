from calc import add, mul

# A distinctive marker the sandbox stdout will carry back in the result
# envelope, so we can prove the tests actually ran in the platform sandbox.
SANDBOX_CONFORMANCE_MARKER = "HYRAX-SANDBOX-CONFORMANCE-OK"


def test_add():
    assert add(2, 3) == 5


def test_mul():
    assert mul(4, 5) == 20


def test_marker(capsys):
    print(SANDBOX_CONFORMANCE_MARKER)
    captured = capsys.readouterr()
    assert "CONFORMANCE-OK" in captured.out
