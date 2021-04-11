import string
import unittest
from random import randint, choice
from auto_check import Node, OrderedList, OrderedStringList

class OrderedListTests(unittest.TestCase):

	def ordered_list_by_arr(self, arr, asc):
	  ordered_list = OrderedList(asc)
	  for x in arr:
	      ordered_list.add(x)
	  return ordered_list

	def ordered_string_list_by_arr(self, arr, asc):
	  ordered_list = OrderedStringList(asc)
	  for x in arr:
	      ordered_list.add(x)
	  return ordered_list

	def check_ordered_list_correct(self, ordered_list):
		if (ordered_list.head is None) and (ordered_list.tail is None):
			return True
		else:
			arr = [x for x in ordered_list]
			arr_reverse = []
			node = ordered_list.tail
			while node is not None:
				arr_reverse.append(node)
				node = node.prev
			return arr == arr_reverse[::-1] \
				and ordered_list.head.prev is None \
				and ordered_list.tail.next is None

	def test_add_in_head_with_true_asc(self):
		ordered_list = self.ordered_list_by_arr([3,5,7], True)
		ordered_list.add(1)
		self.assertEqual([x.value for x in ordered_list], [1,3,5,7])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_tail_with_true_asc(self):
		ordered_list = self.ordered_list_by_arr([3,5,7], True)
		ordered_list.add(9)
		self.assertEqual([x.value for x in ordered_list], [3,5,7,9])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_middle_with_true_asc(self):
		ordered_list = self.ordered_list_by_arr([3,5,7], True)
		ordered_list.add(4)
		self.assertEqual([x.value for x in ordered_list], [3,4,5,7])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_empty_list_with_true_asc(self):
		ordered_list = self.ordered_list_by_arr([], True)
		ordered_list.add(1)
		self.assertEqual([x.value for x in ordered_list], [1])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_head_with_false_asc(self):
		ordered_list = self.ordered_list_by_arr([7,5,3], False)
		ordered_list.add(9)
		self.assertEqual([x.value for x in ordered_list], [9,7,5,3])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_tail_with_false_asc(self):
		ordered_list = self.ordered_list_by_arr([7,5,3], False)
		ordered_list.add(1)
		self.assertEqual([x.value for x in ordered_list], [7,5,3,1])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_middle_with_false_asc(self):
		ordered_list = self.ordered_list_by_arr([7,5,3], False)
		ordered_list.add(4)
		self.assertEqual([x.value for x in ordered_list], [7,5,4,3])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_in_empty_list_with_false_asc(self):
		ordered_list = self.ordered_list_by_arr([], False)
		ordered_list.add(1)
		self.assertEqual([x.value for x in ordered_list], [1])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_add_random(self):
		for _ in range(1000):
			asc = choice([True, False])
			arr = [randint(-5,+5) for _ in range(randint(0,10))]
			ordered_list = self.ordered_list_by_arr(arr, asc)
			test_val = randint(-10,+10)
			arr.append(test_val)
			ordered_list.add(test_val)
			arr.sort(reverse = not asc)
			self.assertEqual([x.value for x in ordered_list], arr)
			self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_find(self):
		ordered_list = self.ordered_list_by_arr([1,2,3], True)
		result = ordered_list.find(1)
		self.assertTrue(isinstance(result, Node))
		self.assertEqual(result.value, 1)

	def test_find_not_included_value(self):
		ordered_list = self.ordered_list_by_arr([1,2,3], True)
		self.assertEqual(ordered_list.find(4), None)

	def test_find_in_empty_list(self):
		ordered_list = self.ordered_list_by_arr([], True)
		self.assertEqual(ordered_list.find(4), None)

	def test_find_random(self):
		for _ in range(1000):
			arr = [randint(-5,+5) for _ in range(randint(0,10))]
			asc = choice([True, False])
			ordered_list = self.ordered_list_by_arr(arr, asc)
			test_val = randint(-10,+10)
			result = ordered_list.find(test_val)
			if test_val in arr:
				self.assertTrue(isinstance(result, Node))
				self.assertEqual(result.value, test_val)
			else:
				self.assertEqual(result, None)

	def test_delete_from_head(self):
		ordered_list = self.ordered_list_by_arr([1,2,3], True)
		ordered_list.delete(1)
		self.assertEqual([x.value for x in ordered_list], [2,3])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_delete_from_tail(self):
		ordered_list = self.ordered_list_by_arr([1,2,3], True)
		ordered_list.delete(3)
		self.assertEqual([x.value for x in ordered_list], [1,2])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_delete_from_middle(self):
		ordered_list = self.ordered_list_by_arr([1,2,3], True)
		ordered_list.delete(2)
		self.assertEqual([x.value for x in ordered_list], [1,3])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_delete_last_elem(self):
		ordered_list = self.ordered_list_by_arr([1], True)
		ordered_list.delete(1)
		self.assertEqual([x.value for x in ordered_list], [])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_delete_not_included_value(self):
		ordered_list = self.ordered_list_by_arr([1,2,3], True)
		ordered_list.delete(4)
		self.assertEqual([x.value for x in ordered_list], [1,2,3])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_delete_from_empty_list(self):
		ordered_list = self.ordered_list_by_arr([], True)
		ordered_list.delete(4)
		self.assertEqual([x.value for x in ordered_list], [])
		self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_delete_random(self):
		for _ in range(1000):
			arr = [randint(-5,+5) for _ in range(randint(0,10))]
			asc = choice([True, False])
			ordered_list = self.ordered_list_by_arr(arr, asc)
			arr.sort(reverse = not asc)
			test_val = randint(-10,+10)
			ordered_list.delete(test_val)
			if test_val in arr:
				arr.remove(test_val)
			self.assertEqual([x.value for x in ordered_list], arr)
			self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_string_add_random(self):
		for _ in range(1000):
			asc = choice([True, False])
			arr = [choice(string.ascii_letters) for _ in range(randint(0,10))]
			ordered_list = self.ordered_string_list_by_arr(arr, asc)
			test_val = choice(string.ascii_letters)
			arr.append(test_val)
			ordered_list.add(test_val)
			arr.sort(reverse = not asc)
			self.assertEqual([x.value for x in ordered_list], arr)
			self.assertTrue(self.check_ordered_list_correct(ordered_list))

	def test_string_find_random(self):
		for _ in range(1000):
			arr = [choice(string.ascii_letters) for _ in range(randint(0,10))]
			asc = choice([True, False])
			ordered_list = self.ordered_string_list_by_arr(arr, asc)
			test_val = choice(string.ascii_letters)
			result = ordered_list.find(test_val)
			if test_val in arr:
				self.assertTrue(isinstance(result, Node))
				self.assertEqual(result.value, test_val)
			else:
				self.assertEqual(result, None)

	def test_string_delete_random(self):
		for _ in range(1000):
			arr = [choice(string.ascii_letters) for _ in range(randint(0,10))]
			asc = choice([True, False])
			ordered_list = self.ordered_string_list_by_arr(arr, asc)
			arr.sort(reverse = not asc)
			test_val = choice(string.ascii_letters)
			ordered_list.delete(test_val)
			if test_val in arr:
				arr.remove(test_val)
			self.assertEqual([x.value for x in ordered_list], arr)
			self.assertTrue(self.check_ordered_list_correct(ordered_list))

if __name__ == '__main__':
	unittest.main()