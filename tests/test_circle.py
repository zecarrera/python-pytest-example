import pytest
import source.shapes as shapes
import math

class TestCircle:

    # the method parameter represents the test method we are about to run
    def setup_method(self, method):
        self.circle = shapes.Circle(10)
        print(f"Seetting up {method}")

    def test_radius(self):
        assert self.circle.radius == 10

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        actual_result = self.circle.perimeter()
        expected_result = 2 * math.pi * self.circle.radius
        assert actual_result == expected_result

    def teardown_method(self, method):
        print(f"Tearing down up {method}")
        del self.circle #not needed for this example, as it would be automatically cleared