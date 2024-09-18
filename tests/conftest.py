import random

import pytest

from source import shapes

#Example of a global fixture, which is then accessible to all test files
@pytest.fixture
def random_rectangle():
    length = random.randint(1, 50)  # Random length between 1 and 50
    width = random.randint(1, 10)   # Random width between 1 and 10
    return shapes.Rectangle(length, width)
