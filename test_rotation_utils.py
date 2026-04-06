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


#print(adjust_rotation(360))

def test_adjust_rotation_100() -> None:
    """Test that 100 stays 100."""
    assert adjust_rotation(100) == 100

def test_adjust_rotation_460() -> None:
    """Test that 460 becomes 100."""
    assert adjust_rotation(460) == 100

def test_adjust_rotation_820() -> None:
    """Test that 820 becomes 100."""
    assert adjust_rotation(820) == 100

def test_adjust_rotation_negative100() -> None:
    """Test that -100 becomes 260."""
    assert adjust_rotation(-100) == 260

def test_adjust_rotation_negative460() -> None:
    """Test that -460 becomes 260."""
    assert adjust_rotation(-460) == 260

def test_adjust_rotation_negative820() -> None:
    """Test that -820 becomes 260."""
    assert adjust_rotation(-820) == 260

def test_adjust_rotation_string_raises_typerror() -> None:
    """Test that a string input raises TypeError."""
    with pytest.raises(TypeError):
        adjust_rotation("asd")



def test_adjust_rotation_zero() -> None:
    """Test that 0 stays 0."""
    assert adjust_rotation(0) == 0


def test_adjust_rotation_360() -> None:
    """Test that 360 becomes 0."""
    assert adjust_rotation(360) == 0


def test_adjust_rotation_720() -> None:
    """Test that 720 becomes 0."""
    assert adjust_rotation(720) == 0


def test_adjust_rotation_float_positive() -> None:
    """Test that a positive float is adjusted correctly."""
    assert adjust_rotation(100.5) == 100.5


def test_adjust_rotation_float_negative() -> None:
    """Test that a negative float is adjusted correctly."""
    assert adjust_rotation(-45.5) == 314.5