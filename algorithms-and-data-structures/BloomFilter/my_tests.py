import unittest
from code_for_auto_tests import BloomFilter


class BloomFilterTests(unittest.TestCase):

	def test_regression(self):
		bloom = BloomFilter(32)
		bloom.add('0123456789')
		self.assertTrue(bloom.is_value('0123456789'))
		self.assertFalse(bloom.is_value('1234567890'))

	def test_random(self):
		bloom_set = BloomFilter(32)
		native_set = set()
		string = '0123456789'
		test_data = set()
		for _ in string:
			string = string[1:] + string[0]
			test_data.add(string)

		for val in test_data:
			native_set.add(val)
			bloom_set.add(val)
			for test_val in native_set:
				self.assertTrue(bloom_set.is_value(test_val))


if __name__ == '__main__':
	unittest.main()