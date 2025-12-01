import pytest
from unittest.mock import patch
from guess_the_number import getMinValue, getMaxValue, getUserGuess

# testing getMinValue() function
def testMinValue():
    # using patch to mock input function
    
    for i in range(1, 11):
        with patch("builtins.input", return_value=f"{i}"):
            assert getMinValue() == i
            
def testMinValueNotValid():
    with patch("builtins.input", return_value="abc"):
        with pytest.raises(ValueError):
            getMinValue()
            
def testMinValueWithWhitespace():
    with patch("builtins.input", return_value="    1    "):
        assert getMinValue() == 1


# testing getMaxValue() function
def testMaxValue():
    for i in range(1, 11):
        with patch("builtins.input", return_value=f"{i}"):
            assert getMaxValue() == i

def testMaxValueNotValid():
    with patch("builtins.input", return_value="abc"):
        with pytest.raises(ValueError):
            getMaxValue()
            
def testMaxValueWithWhitespace():
    with patch("builtins.input", return_value="    1    "):
        assert getMaxValue() == 1
        
# testing getUserGuess() function
def testUserGuess():
    with patch("builtins.input", return_value="7"):
        assert getUserGuess(1, 10) == 7
        
def testUserGuessNotValid():
    with patch("builtins.input", return_value="abc"):
        with pytest.raises(ValueError):
            getUserGuess(1, 5)
        
def testUserGuessWithWhitespace():
    with patch("builtins.input", return_value="    15    "):
        assert getUserGuess(1, 20) == 15