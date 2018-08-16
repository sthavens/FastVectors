import pytest
from FastVectors import FastVectors

def test_pytest():
    assert 1 == 1

def test_canInitializeFastVectors():
    fv = FastVectors()
    assert FastVectors == type(fv)