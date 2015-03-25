
#
# Author: Erica Pisani
# Date: March 25, 2015
#

import unittest
import demoSource as src

class TestDemoSource(unittest.TestCase):
    def setUp(self):
        self.numA = 10
        self.numB = 3

    def test_add_success(self):
        result = src.add(5, 2)
        self.assertEqual(result, 7)

    def test_add_with_fixtures_success(self):
        result = src.add(self.numA, self.numB)
        self.assertEqual(result, 13)

    def test_multiply_success(self):
        result = src.multiply(3, 2)
        self.assertEqual(result, 6)

    def test_multiply_with_fixtures_success(self):
        result = src.multiply(self.numA, self.numB)
        self.assertEqual(result, 30)

    def test_divide_success(self):
        result = src.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_with_fixtures_success(self):
        result = src.divide(self.numA, self.numB)
        self.assertEqual(result, 3)

    def test_subtract_success(self):
        result = src.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_with_fixtures_success(self):
        result = src.subtract(self.numA, self.numB)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
