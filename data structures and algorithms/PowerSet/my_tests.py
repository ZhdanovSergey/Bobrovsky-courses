import random
import time
import unittest
from code_for_auto_tests import PowerSet


class PowerSetTestsUtils():

	def create_power_set_by_arr(self, arr):
		power_set = PowerSet()
		for x in arr:
			power_set.put(x)
		return power_set

	def check_power_set_content(self, power_set, arr):
		if power_set.size() != len(arr):
			return False
		for x in arr:
			if not power_set.get(x):
				return False
		return True

class PowerSetTests(unittest.TestCase, PowerSetTestsUtils):

	def test_put_existed_value(self):
		power_set = self.create_power_set_by_arr([1,2,3])
		power_set.put(3)
		self.assertTrue(self.check_power_set_content(power_set, [1,2,3]))

	def test_put_not_existed_value(self):
		power_set = self.create_power_set_by_arr([1,2,3])
		power_set.put(4)
		self.assertTrue(self.check_power_set_content(power_set, [1,2,3,4]))

	def test_remove_existed_value(self):
		power_set = self.create_power_set_by_arr([1,2,3])
		method_return = power_set.remove(3)
		self.assertTrue(self.check_power_set_content(power_set, [1,2]))
		self.assertTrue(method_return)

	def test_remove_not_existed_value(self):
		power_set = self.create_power_set_by_arr([1,2,3])
		method_return = power_set.remove(4)
		self.assertTrue(self.check_power_set_content(power_set, [1,2,3]))
		self.assertFalse(method_return)

	def test_intersection_with_empty_result(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([4,5,6])
		result_set = power_set1.intersection(power_set2)
		self.assertTrue(self.check_power_set_content(result_set, []))

	def test_intersection_with_not_empty_result(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([1,2,4])
		result_set = power_set1.intersection(power_set2)
		self.assertTrue(self.check_power_set_content(result_set, [1,2]))

	def test_union_with_empty_set(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([])
		result_set = power_set1.union(power_set2)
		self.assertTrue(self.check_power_set_content(result_set, [1,2,3]))

	def test_union_with_not_empty_set(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([1,2,3,4])
		result_set = power_set1.union(power_set2)
		self.assertTrue(self.check_power_set_content(result_set, [1,2,3,4]))

	def test_difference_with_empty_result(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([1,2,3])
		result_set = power_set1.difference(power_set2)
		self.assertTrue(self.check_power_set_content(result_set, []))

	def test_difference_with_not_empty_result(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([1,2])
		result_set = power_set1.difference(power_set2)
		self.assertTrue(self.check_power_set_content(result_set, [3]))

	def test_issubset_all_param_elements_included(self):
		power_set1 = self.create_power_set_by_arr([1,2,3,4,5])
		power_set2 = self.create_power_set_by_arr([1,2,3])
		self.assertTrue(power_set1.issubset(power_set2))

	def test_issubset_all_current_elements_included_in_param(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([1,2,3,4,5])
		self.assertFalse(power_set1.issubset(power_set2))

	def test_issubset_not_all_param_elements_included(self):
		power_set1 = self.create_power_set_by_arr([1,2,3])
		power_set2 = self.create_power_set_by_arr([1,4])
		self.assertFalse(power_set1.issubset(power_set2))


def create_big_power_set(size):
		power_set = PowerSet()
		for i in range(size):
			power_set.put(i)
		return power_set

big_power_set = create_big_power_set(20_000)


class PowerSetSpeedTests(unittest.TestCase, PowerSetTestsUtils):

	def setUp(self):
		self._started_at = time.time()

	def tearDown(self):
		elapsed = time.time() - self._started_at
		print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

	def test_put_speed(self):
		big_power_set.put(random.randint(0,big_power_set.size()*2))

	def test_remove_speed(self):
		big_power_set.remove(random.randint(0,big_power_set.size()*2))

	def test_intersection_speed(self):
		result_set = big_power_set.intersection(self.create_power_set_by_arr([random.randint(0,big_power_set.size()*2) for _ in range(1000)]))

	def test_union_speed(self):
		result_set = big_power_set.union(self.create_power_set_by_arr([random.randint(0,big_power_set.size()*2) for _ in range(1000)]))

	def test_difference_speed(self):
		result_set = big_power_set.difference(self.create_power_set_by_arr([random.randint(0,big_power_set.size()*2) for _ in range(1000)]))

	def test_issubset_speed(self):
		result_set = big_power_set.issubset(self.create_power_set_by_arr([random.randint(0,big_power_set.size()*2) for _ in range(1000)]))

if __name__ == '__main__':
	unittest.main()