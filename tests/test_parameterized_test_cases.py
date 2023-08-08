import pytest

def test_multiply_two_positive_ints():
    assert 2 * 3 == 6

def test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0


# refactor above repetitive test cases

products = [
    (2, 3, 6),          # positive integers
    (1, 99, 99),        # identity
    (0, 99, 0),         # zero
    (3, -4, -12),       # positive by negative
    (-5, -5, 25),       # negative by negative
    (2.5, 6.7, 16.75)   # floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


# NOTE: File name 