#print("gelloworld")

"""
Docstring for test_rotaion_utils.py
i. LAB 11: Unit Testing
ii. Sam Cocquyt
iii. Create a new test file and write a complete set of pytest tests to ensure the provided function works exactly as specified
iv. No starter code
v. 4/5/2026
"""

import pytest
from rotation_utils import adjust_rotation


print(adjust_rotation(360))

def test_adjust_rotation_100():
    assert adjust_rotation(100) == 100

def test_adjust_rotation_460():
    assert adjust_rotation(460) == 100

def test_adjust_rotation_820():
    assert adjust_rotation(820) == 100

def test_adjust_rotation_negative100():
    assert adjust_rotation(-100) == 260

def test_adjust_rotation_negative460():
    assert adjust_rotation(-460) == 260

def test_adjust_rotation_negative820():
    assert adjust_rotation(-820) == 260

def test_adjust_rotation_string_raises_typerror():
    with pytest.raises(TypeError):
        adjust_rotation("asd")



def test_adjust_rotation_zero():
    assert adjust_rotation(0) == 0


def test_adjust_rotation_360():
    assert adjust_rotation(360) == 0


def test_adjust_rotation_720():
    assert adjust_rotation(720) == 0


def test_adjust_rotation_float_positive():
    assert adjust_rotation(100.5) == 100.5


def test_adjust_rotation_float_negative():
    assert adjust_rotation(-45.5) == 314.5