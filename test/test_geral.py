import math
import pytest


def raiz(n):
    return math.sqrt(n)


def test_raiz():
    assert raiz(9) == 3
    assert raiz(81) == 9
    assert raiz(144) == 12
    assert raiz(400) == 20
    assert raiz(196) == 14


def eh_palindromo(s):
    return s == s[::-1]


@pytest.mark.parametrize(
    "input, expected",
    [
        ("radar", True),
        ("refer", True),
        ("subi no onibus", False),
        ("python", False),
        ("", True),
    ],
)
def teste_eh_palindromo(input, expected):
    assert eh_palindromo(input) == expected
