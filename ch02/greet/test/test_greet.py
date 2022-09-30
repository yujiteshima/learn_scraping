
from greet.greet import greet


def test_greet():
    result = greet()
    assert result == "Hello, World!"