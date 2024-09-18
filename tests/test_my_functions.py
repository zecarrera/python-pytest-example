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
