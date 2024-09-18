import time

import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 2)
    assert result == 3

def test_add_strings():
    result = my_functions.add("test", "one")
    assert result == "testone"

def test_divide():
    result = my_functions.divide(4,2)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        my_functions.divide(2, 0)
    assert str(exc_info.value).__contains__("Division by zero not allowed")

# Example of pytest's tagging, using custom tag
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

# Example of  tagging to skip a test
@pytest.mark.skip(reason ="feature is still WIP")
def test_multiply():
    assert my_functions.multiply(1,1) == 1

# xfail TAG can be used to mark a test that we know will fail, for example due to code that has not yet been fixed.
# this prevents the test suite from failing entirely due to this known issue
@pytest.mark.xfail(reason="Forcing failure")
def test_divide_zero_broken():
    my_functions.divide(3,0)