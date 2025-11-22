import sys
import os
import pytest
from unittest.mock import patch

# Add parent folder to sys.path to import your madlibs.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from madlibs import getUserInput, checkIfAlphabet, madlib, main

# ------------------------------
# Test checkIfAlphabet function
# ------------------------------
def test_check_alphabet_valid():
    assert checkIfAlphabet("happy", "run", "jump", "Elon Musk")

def test_check_alphabet_invalid_numbers():
    assert not checkIfAlphabet("happy1", "run", "jump", "Elon Musk")

def test_check_alphabet_invalid_symbols():
    assert not checkIfAlphabet("happy!", "run", "jump", "Elon Musk")

# ------------------------------
# Test madlib function
# ------------------------------
def test_madlib_output():
    result = madlib("happy", "run", "jump", "Elon Musk")
    assert "Computer progamming is so happy!" in result
    assert "I love to run." not in result  # optional check

# ------------------------------
# Test getUserInput with mocked input
# ------------------------------
@patch('builtins.input', side_effect=["happy", "run", "jump", "Elon Musk"])
def test_getUserInput(mock_inputs):
    adj, verb1, verb2, famous_person = getUserInput()
    assert (adj, verb1, verb2, famous_person) == ("Happy", "Run", "Jump", "Elon Musk")

# ------------------------------
# Test main game loop for 'play again = n'
# ------------------------------
@patch('builtins.input', side_effect=["happy", "run", "jump", "Elon Musk", "n"])
def test_main_single_round(mock_inputs, capsys):
    # Run main() once
    main()
    captured = capsys.readouterr()
    assert "Computer progamming is so Happy!" in captured.out

# ------------------------------
# Test main game loop for invalid input
# ------------------------------
@patch('builtins.input', side_effect=["happy1", "run", "jump", "Elon Musk", "n"])
def test_main_invalid_input(mock_inputs, capsys):
    # Run main() once
    main()
    captured = capsys.readouterr()
    assert "Please enter alphabets only not other type of value" in captured.out