# test_calculator.py
import unittest
from some_package.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    # Test for the 'add' function
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # Test for the 'subtract' function
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(10, -5), 15)
    
    # Test for the 'multiply' function
    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)

    # Test for the 'divide' function
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 2), -5)
    
    # Test the error case for dividing by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()