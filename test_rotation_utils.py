print("gelloworld")

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

def test_adjust_rotation_100():
    assert adjust_rotation(100) == 100

def test_adjust_rotation_460():
    assert adjust_rotation(460) == 100

def test_adjust_rotation_negative100():
    assert adjust_rotation(-100) == 260

def test_adjust_rotation_negative460():
    assert adjust_rotation(-460) == 260