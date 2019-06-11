import pytest
from FastVectors import FastVectors, Vector

def test_vector_creation():
    vec = Vector([1,2,3])
    assert Vector == type(vec)

def test_addition():
    a = Vector([1,2,3])
    b = Vector([4,5,6])
    assert a + b == Vector([5,7,9])

def test_addition_with_different_sizes_throws_error():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6, 7])
    with pytest.raises(AssertionError):
        assert a + b

def test_subtraction():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    assert a - b == Vector([-3, -3, -3])

def test_subtraction_with_different_sizes_throws_error():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6, 7])
    with pytest.raises(AssertionError):
        assert a - b

def test_scalar_multiplication():
    a = Vector([1, 2, 3])
    b = 3
    assert a * b == Vector([2, 4, 6])