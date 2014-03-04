
#
# Author: Erica Pisani
# Date: March 5, 2014
#

import unittest
import demoSource as src

class TestDemoSource(unittest.TestCase):

	def setUp(self):
		self.numA = 4
		self.numB = 5

	def test_addNumbers(self):
		result = src.add(self.numA, self.numB)
		self.assertEqual(result, 9)

	def test_subtractNumbers(self):
		result = src.subtract(self.numA, self.numB)
		self.assertEqual(result, -1)

	def test_multiplyNumbers(self):
		result = src.multiply(self.numA, self.numB)
		self.assertEqual(result, 20)

	def test_multiplyNegativeNumbers(self):
		result = src.multiply(-1, self.numA)
		self.assertEqual(result, -4)

	def test_divideNumbers(self):
		result = src.divide(self.numB, self.numA)
		self.assertEqual(result, 1)

	def test_divideByZero(self):
		self.assertRaises(ZeroDivisionError, src.divide, self.numA, 0)

if __name__ == '__main__':
	unittest.main()
