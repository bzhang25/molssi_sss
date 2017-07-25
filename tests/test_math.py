"""
Testing for the math.py module 
"""

import molssi_sss as ms 
import pytest

def test_add():
    assert ms.add(5,2) == 7
    assert ms.add(2,5) == 7

def test_mult():
    assert ms.mult(2,5) == 10
    assert ms.mult(5,2) == 10

def test_divide():
    assert ms.divide(5.0,2.0) == 2.5

def test_subtract():
    assert ms.subtract(2,5) == -3
    assert ms.subtract(5,2) == 3

def test_mod():
    assert ms.mod(2,7) == 2
    assert ms.mod(3,3) == 0
    assert ms.mod(7,2) == 1
