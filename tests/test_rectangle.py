import pytest

import source.shapes as shapes
from tests.conftest import random_rectangle

# Example of pytest fixture utilisation, visible only within this file scope
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(5, 2)

# Example using a fixture to provide multiple inputs to a test case
@pytest.fixture
def edge_case_data():
    return [
        (0, 0, 0, False),          # Zero dimensions
        (0, 5, 0, False),          # Zero length
        (5, 0, 0, False),          # Zero width
        (-1, -1, None, True),      # Negative dimensions
        (-1, 5, None, True),       # Negative length
        (5, -1, None, True),       # Negative width
        (1e6, 1e6, 1e12, False),   # Large values
        (3.5, 2.0, 7.0, False),    # Floating point values
    ]

def test_area(my_rectangle):
    assert my_rectangle.area() == 10

def test_perimeter(my_rectangle):
    actual_result = my_rectangle.perimeter()
    expected_result = 14
    assert actual_result == expected_result

# Example using data provided from the conftest global fixture file
def test_not_equal_rectangles(my_rectangle, random_rectangle):
    assert my_rectangle != random_rectangle

# Example using multiple inputs from a single fixture method
def test_area_edge_cases(edge_case_data):
    for length, width, expected_area, should_raise in edge_case_data:
        if should_raise:
            with pytest.raises(ValueError):
                shapes.Rectangle(length, width)
        else:
            rect = shapes.Rectangle(length, width)
            assert rect.area() == expected_area