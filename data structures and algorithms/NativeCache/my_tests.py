import unittest
import random
import string
from code_for_auto_tests import NativeCache


class NativeCacheTests(unittest.TestCase):

	def test_hash_fun(self):
		table = NativeCache(17)
		test_key = '123'
		index = table.hash_fun(test_key)
		self.assertTrue(isinstance(index, int))
		self.assertTrue(0 <= index < 17)

	def test_hash_fun_random(self):
		for _ in range(1000):
			size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
			table = NativeCache(size)
			test_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,100)))
			index = table.hash_fun(test_key)
			self.assertTrue(isinstance(index, int))
			self.assertTrue(0 <= index < size)

	def test_put_new_key(self):
		table = NativeCache(17)
		test_key = '123'
		test_val = 'abc'
		table.put(test_key, test_val)
		self.assertTrue(test_key in table.slots)
		self.assertTrue(test_val in table.values)
		self.assertEqual(table.slots.index(test_key), table.values.index(test_val))

	def test_put_existed_key(self):
		table = NativeCache(17)
		test_key = '123'
		test_val_1 = 'abc'
		test_val_2 = 'abcd'
		table.put(test_key, test_val_1)
		table.put(test_key, test_val_2)
		self.assertTrue(test_key in table.slots)
		self.assertTrue(test_val_1 not in table.values)
		self.assertTrue(test_val_2 in table.values)
		self.assertEqual(table.slots.index(test_key), table.values.index(test_val_2))

	def test_put_overflow(self):
		size = 17
		table = NativeCache(size)
		for i in range(size):
			table.put(str(i), i)
			if i != 10:
				table.get(str(i))
		min_hits_index = table.hits.index(min(table.hits))
		test_key = '123'
		test_val = 'abc'
		table.put(test_key, test_val)
		self.assertTrue(test_key in table.slots)
		self.assertTrue(test_val in table.values)
		self.assertEqual(table.slots.index(test_key), table.values.index(test_val))
		self.assertEqual(table.slots.index(test_key), min_hits_index)

	def test_put_random(self):
		for _ in range(100):
			size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
			table = NativeCache(size)
			for _ in range(table.size * 2):
				test_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,10)))
				test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,10)))
				is_overflow = False
				if None not in table.slots \
					and test_key not in table.slots:
					is_overflow = True
					min_hits_index = table.hits.index(min(table.hits))
				table.put(test_key, test_val)
				self.assertTrue(test_key in table.slots)
				self.assertTrue(test_val in table.values)
				self.assertEqual(table.values[table.slots.index(test_key)], test_val)
				if is_overflow:
					self.assertEqual(table.slots[min_hits_index], test_key)

	def test_is_key_existed(self):
		table = NativeCache(17)
		test_key = '123'
		test_val = 'abc'
		table.put(test_key, test_val)
		self.assertTrue(table.is_key(test_key))

	def test_is_key_not_existed(self):
		table = NativeCache(17)
		test_key = '123'
		self.assertFalse(table.is_key(test_key))

	def test_is_key_random(self):
		for _ in range(100):
			size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
			table = NativeCache(size)
			for _ in range(table.size):
				test_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,10)))
				test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,10)))
				table.put(test_key, test_val)
				is_key_exist = random.choice([True, False])
				if is_key_exist:
					test_key = random.choice(table.slots)
					self.assertTrue(table.is_key(test_key))
				else:
					test_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
					self.assertFalse(table.is_key(test_key))

	def test_get_existed(self):
		table = NativeCache(17)
		test_key = '123'
		test_val = 'abc'
		table.put(test_key, test_val)
		self.assertEqual(table.get(test_key), test_val)
		self.assertEqual(table.hits[table.slots.index(test_key)], 1)

	def test_get_not_existed(self):
		table = NativeCache(17)
		test_key = '123'
		self.assertEqual(table.get(test_key), None)

	def test_get_random(self):
		for _ in range(100):
			size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
			table = NativeCache(size)
			for _ in range(table.size):
				test_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,10)))
				test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,10)))
				table.put(test_key, test_val)
				is_key_exist = random.choice([True, False])
				if is_key_exist:
					test_key = random.choice(table.slots)
					test_val = table.values[table.slots.index(test_key)]
					hits_counter_before_get = table.hits[table.slots.index(test_key)]
					get_result = table.get(test_key)
					hits_counter_after_get = table.hits[table.slots.index(test_key)]
					self.assertEqual(get_result, test_val)
					self.assertTrue(hits_counter_before_get == hits_counter_after_get - 1)
				else:
					test_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
					self.assertEqual(table.get(test_key), None)


if __name__ == '__main__':
	unittest.main()