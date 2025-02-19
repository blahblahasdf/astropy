import pytest
from ..main import say_hello

def test_say_hello(capsys):
    """Test that say_hello prints the expected message."""
    say_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
