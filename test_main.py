import unittest
import math
from main import sqrt, factorial, ln, power

class TestCalculator(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(sqrt(16), 4.0)
        self.assertEqual(sqrt(0), 0.0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_ln(self):
        self.assertAlmostEqual(ln(math.e), 1.0, places=5)
        self.assertAlmostEqual(ln(1), 0.0, places=5)

    def test_power(self):
        self.assertEqual(power(2, 3), 8.0)
        self.assertEqual(power(5, 0), 1.0)
        self.assertEqual(power(9, 0.5), 3.0)

if __name__ == "__main__":
    unittest.main()
