import pytest
from unittest.mock import patch

from guess_the_number import getMinValue
def testMinValue():
    assert getMinValue() == type(int)