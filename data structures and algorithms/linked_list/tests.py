import unittest
from random import choice, randint
from exercise_1_6 import Node, LinkedList
from exercise_8 import get_sum_of_lists

def linked_list_by_array_of_values(arr):
  linked_list = LinkedList()
  for x in arr:
      linked_list.add_in_tail(Node(x))
  return linked_list

def linked_list_by_array_of_nodes(arr):
  linked_list = LinkedList()
  for x in arr:
  	linked_list.add_in_tail(x)
  return linked_list

def check_linked_list_tail_correct(linked_list):
	prev_node = None
	for node in linked_list:
		prev_node = node
	return prev_node == linked_list.tail

class LinkedListTests(unittest.TestCase):

	def test_single_deletion_regression(self):
		linked_list = linked_list_by_array_of_values([1,2,3,4,5])
		linked_list.delete(3)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1,2,4,5])

	def test_single_deletion_first_elem(self):
		linked_list = linked_list_by_array_of_values([1,2,3,4,5])
		linked_list.delete(1)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [2,3,4,5])

	def test_single_deletion_last_elem(self):
		linked_list = linked_list_by_array_of_values([1,2,3,4,5])
		linked_list.delete(5)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1,2,3,4])

	def test_single_deletion_with_empty_result(self):
		linked_list = linked_list_by_array_of_values([1])
		linked_list.delete(1)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [])

	def test_single_deletion_first_elem_with_single_elem_result(self):
		linked_list = linked_list_by_array_of_values([1,2])
		linked_list.delete(1)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [2])

	def test_single_deletion_last_elem_with_single_elem_result(self):
		linked_list = linked_list_by_array_of_values([1,2])
		linked_list.delete(2)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1])

	def test_single_deletion_random(self):
		for i in range(1000):
			arr = []
			for i in range(randint(1,100)):
				arr.append(randint(-10,+10))
			test_val = choice(arr)
			linked_list = linked_list_by_array_of_values(arr)
			linked_list.delete(test_val)
			arr.remove(test_val)
			self.assertTrue(check_linked_list_tail_correct(linked_list))
			self.assertEqual([x.value for x in linked_list], arr)

	def test_multiple_deletion_regression(self):
		linked_list = linked_list_by_array_of_values([1,2,3,3,3,4,5])
		linked_list.delete(3, all=True)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1,2,4,5])

	def test_multiple_deletion_with_empty_result(self):
		linked_list = linked_list_by_array_of_values([1,1,1,1,1,1])
		linked_list.delete(1, all=True)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [])

	def test_multiple_deletion_random(self):
		for i in range(1000):
			arr = []
			for i in range(randint(1,100)):
				arr.append(randint(-5,+5))
			test_val = choice(arr)
			linked_list = linked_list_by_array_of_values(arr)
			linked_list.delete(test_val, all=True)
			ans_arr = [x for x in arr if x != test_val]
			self.assertTrue(check_linked_list_tail_correct(linked_list))
			self.assertEqual([x.value for x in linked_list], ans_arr)

	def test_clean_regression(self):
		linked_list = linked_list_by_array_of_values([1,2,3,4,5])
		linked_list.clean()
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [])

	def test_find_all_regression(self):
		node1 = Node(1)
		node2 = Node(1)
		node3 = Node(3)
		nodes_arr = [node1, node2, node3]
		linked_list = linked_list_by_array_of_nodes(nodes_arr)
		test_val = 1
		output_arr = linked_list.find_all(test_val)
		self.assertEqual(output_arr, [node1, node2])

	def test_find_all_not_included_value(self):
		nodes_arr = [Node(x) for x in [1,2,3]]
		linked_list = linked_list_by_array_of_nodes(nodes_arr)
		test_val = 5
		output_arr = linked_list.find_all(test_val)
		self.assertEqual(output_arr, [])

	def test_find_all_in_empty_list(self):
		linked_list = LinkedList()
		test_val = 5
		output_arr = linked_list.find_all(test_val)
		self.assertEqual(output_arr, [])

	def test_find_all_random(self):
		for i in range(1000):
			nodes_arr = []
			for i in range(randint(1,100)):
				nodes_arr.append(Node(randint(-10,+10)))
			test_val = choice(nodes_arr).value
			linked_list = linked_list_by_array_of_nodes(nodes_arr)
			output_arr = linked_list.find_all(test_val)
			ans_arr = [x for x in nodes_arr if x.value == test_val]
			self.assertEqual(output_arr, ans_arr)

	def test_len_regression(self):
		linked_list = linked_list_by_array_of_values([1,2,3,4,5])
		self.assertEqual(linked_list.len(), 5)

	def test_len_of_empty_list(self):
		linked_list = LinkedList()
		self.assertEqual(linked_list.len(), 0)

	def test_len_random(self):
		for i in range(1000):
			arr = []
			for i in range(randint(1,100)):
				arr.append(randint(-10,+10))
			linked_list = linked_list_by_array_of_values(arr)
			self.assertEqual(linked_list.len(), len(arr))

	def test_insert_regression(self):
		node1 = Node(1)
		node2 = Node(2)
		node3 = Node(3)
		linked_list = linked_list_by_array_of_nodes([node1, node2])
		linked_list.insert(node1, node3)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1, node3, node2])

	def test_insert_first_elem(self):
		node1 = Node(1)
		node2 = Node(2)
		node3 = Node(3)
		linked_list = linked_list_by_array_of_nodes([node1, node2])
		linked_list.insert(None, node3)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node3, node1, node2])

	def test_insert_last_elem(self):
		node1 = Node(1)
		node2 = Node(2)
		node3 = Node(3)
		linked_list = linked_list_by_array_of_nodes([node1, node2])
		linked_list.insert(node2, node3)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1, node2, node3])

	def test_insert_in_empty_list(self):
		node1 = Node(1)
		linked_list = LinkedList()
		linked_list.insert(None, node1)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1])

	def test_insert_random(self):
		for i in range(1000):
			nodes_arr = []
			for i in range(randint(1,100)):
				nodes_arr.append(Node(randint(-10,+10)))
		linked_list = linked_list_by_array_of_nodes(nodes_arr)
		after_node = choice(nodes_arr)
		test_node = Node(100)
		linked_list.insert(after_node, test_node)
		nodes_arr.insert(nodes_arr.index(after_node) + 1, test_node)
		self.assertTrue(check_linked_list_tail_correct(linked_list))
		self.assertEqual([x for x in linked_list], nodes_arr)

	def test_sum_of_lists_regression(self):
		linked_list1 = linked_list_by_array_of_values([1,2,3])
		linked_list2 = linked_list_by_array_of_values([4,5,6])
		linked_list_sum = get_sum_of_lists(linked_list1, linked_list2)
		self.assertEqual([x.value for x in linked_list_sum], [5,7,9])

	def test_sum_of_lists_with_different_len(self):
		linked_list1 = linked_list_by_array_of_values([1,2,3])
		linked_list2 = linked_list_by_array_of_values([4,5,6,7])
		linked_list_sum = get_sum_of_lists(linked_list1, linked_list2)
		self.assertTrue(linked_list_sum is None)

	def test_sun_of_lists_random(self):
		for i in range(1000):
			arr1 = []
			arr2 = []
			for i in range(randint(1,100)):
				arr1.append(randint(-10,+10))
				arr2.append(randint(-10,+10))
			for i in range(0 if randint(0,10) == 0 else randint(1,100)):
				arr2.append(randint(-10,+10))
			linked_list1 = linked_list_by_array_of_values(arr1)
			linked_list2 = linked_list_by_array_of_values(arr2)
			linked_list_sum = get_sum_of_lists(linked_list1, linked_list2)
			if len(arr1) == len(arr2):
				ans_arr = []
				for i in range(len(arr1)):
					ans_arr.append(arr1[i] + arr2[i])
				self.assertEqual([x.value for x in linked_list_sum], ans_arr)
			else:
				self.assertTrue(linked_list_sum is None)

	def test_iteration_regression(self):
		orig_arr = [1,2,3,4,5]
		linked_list = linked_list_by_array_of_values(orig_arr)
		result_arr = []
		for x in linked_list:
			result_arr.append(x.value)
		self.assertEqual(orig_arr, result_arr)

	def test_iteration_empty_list(self):
		orig_arr = []
		linked_list = linked_list_by_array_of_values(orig_arr)
		result_arr = []
		for x in linked_list:
			result_arr.append(x.value)
		self.assertEqual(orig_arr, result_arr)

	def test_iteration_random(self):
		for i in range(1000):
			orig_arr = []
			for i in range(randint(0,100)):
				orig_arr.append(randint(-10,+10))
			linked_list = linked_list_by_array_of_values(orig_arr)
			result_arr = []
			for x in linked_list:
				result_arr.append(x.value)
			self.assertEqual(orig_arr, result_arr)

if __name__ == '__main__':
	unittest.main()