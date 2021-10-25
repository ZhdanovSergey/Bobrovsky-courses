import unittest
import random
from code import GenerateBBSTArray


class aBSTTests(unittest.TestCase):
	def test_empty(self):
		result = GenerateBBSTArray([])
		self.assertTrue(result == [], result)

	def test_oneKey(self):
		result = GenerateBBSTArray([0])
		self.assertTrue(result == [0], result)

	def test_twoKeys(self):
		result = GenerateBBSTArray([0, 1])
		self.assertTrue(result == [1, 0, None], result)

	def test_threeKeys(self):
		result = GenerateBBSTArray([0, 1, 2])
		self.assertTrue(result == [1, 0, 2], result)

	def test_fourKeys(self):
		result = GenerateBBSTArray([0, 1, 2, 3])
		self.assertTrue(result == [2, 1, 3, 0, None, None, None], result)

	def test_fiveKeys(self):
		result = GenerateBBSTArray([0, 1, 2, 3, 4])
		self.assertTrue(result == [2, 1, 4, 0, None, 3, None], result)

	def test_sixKeys(self):
		result = GenerateBBSTArray([0, 1, 2, 3, 4, 5])
		self.assertTrue(result == [3, 1, 5, 0, 2, 4, None], result)

	def test_sevenKeys(self):
		result = GenerateBBSTArray([0, 1, 2, 3, 4, 5, 6])
		self.assertTrue(result == [3, 1, 5, 0, 2, 4, 6], result)

	def test_eightKeys(self):
		result = GenerateBBSTArray([0, 1, 2, 3, 4, 5, 6, 7])
		self.assertTrue(result == [4, 2, 6, 1, 3, 5, 7, 0, None, None, None, None, None, None, None], result)

if __name__ == '__main__':
	unittest.main()