# Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class 
# that supports addition, subtraction, multiplication, and division operations.

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        """Test the addition method."""
        calc = SimpleCalculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(3.5, 2.5), 6.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(5, 2), 3)
        self.assertEqual(calc.subtract(-2, -3), 1)
        self.assertEqual(calc.subtract(3.5, 1.0), 2.5)

    def test_multiplication(self):
        """Test the multiplication method."""
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(4, 3), 12)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the division method."""
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(10, 2), 5.0)
        self.assertEqual(calc.divide(9, 3), 3.0)
        self.assertEqual(calc.divide(5.0, 2.0), 2.5)
        self.assertEqual(calc.divide(10, 0), None)  # Division by zero

if __name__ == '__main__':
    unittest.main()

