import unittest
from random import choice, randint
from auto_check import Node, LinkedList2

def linked_list_2_by_values_arr(arr):
  linked_list = LinkedList2()
  for x in arr:
      linked_list.add_in_tail(Node(x))
  return linked_list

def linked_list_2_by_nodes_arr(arr):
  linked_list = LinkedList2()
  for x in arr:
  	linked_list.add_in_tail(x)
  return linked_list

def check_linked_list_2_correct(linked_list):
	if (linked_list.head is None) and (linked_list.tail is None):
		return True
	else:
		arr = [x for x in linked_list]
		arr_reverse = []
		node = linked_list.tail
		while node is not None:
			arr_reverse.append(node)
			node = node.prev
		return arr == arr_reverse[::-1] \
			and linked_list.head.prev is None \
			and linked_list.tail.next is None

class LinkedList2Tests(unittest.TestCase):

	def test_iteration_regression(self):
		orig_arr = [1,2,3,4,5]
		linked_list = linked_list_2_by_values_arr(orig_arr)
		self.assertEqual(orig_arr, [x.value for x in linked_list])

	def test_iteration_empty_list(self):
		orig_arr = []
		linked_list = linked_list_2_by_values_arr(orig_arr)
		self.assertEqual(orig_arr, [x.value for x in linked_list])

	def test_iteration_random(self):
		for i in range(1000):
			values_arr = [randint(-10,+10) for j in range(randint(0,100))]
			linked_list = linked_list_2_by_values_arr(values_arr)
			self.assertEqual(values_arr, [x.value for x in linked_list])

	def test_find_regression(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2, node3])
		test_val = 2
		output_node = linked_list.find(test_val)
		self.assertEqual(output_node, node2)

	def test_find_first_elem(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2, node3])
		test_val = 1
		output_node = linked_list.find(test_val)
		self.assertEqual(output_node, node1)

	def test_find_last_elem(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2, node3])
		test_val = 3
		output_node = linked_list.find(test_val)
		self.assertEqual(output_node, node3)

	def test_find_not_included_value(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2, node3])
		test_val = 5
		output_node = linked_list.find(test_val)
		self.assertTrue(output_node is None)

	def test_find_in_empty_list(self):
		linked_list = LinkedList2()
		test_val = 5
		output_node = linked_list.find(test_val)
		self.assertTrue(output_node is None)

	def test_find_random(self):
		for i in range(1000):
			nodes_arr = [Node(randint(-10,+10)) for j in range(randint(0,100))]
			if len(nodes_arr) > 0:
				test_val = choice(nodes_arr).value
				ans_node = next(x for x in nodes_arr if x.value == test_val)
			else:
				test_val = 100
				ans_node = None
			linked_list = linked_list_2_by_nodes_arr(nodes_arr)
			output_node = linked_list.find(test_val)
			self.assertEqual(output_node, ans_node)

	def test_find_all_regression(self):
		node1, node2, node3 = (Node(x) for x in [1,1,3])
		nodes_arr = [node1, node2, node3]
		linked_list = linked_list_2_by_nodes_arr(nodes_arr)
		test_val = 1
		output_arr = linked_list.find_all(test_val)
		self.assertEqual(output_arr, [node1, node2])

	def test_find_all_not_included_value(self):
		nodes_arr = [Node(x) for x in [1,2,3]]
		linked_list = linked_list_2_by_nodes_arr(nodes_arr)
		test_val = 5
		output_arr = linked_list.find_all(test_val)
		self.assertEqual(output_arr, [])

	def test_find_all_in_empty_list(self):
		linked_list = LinkedList2()
		test_val = 5
		output_arr = linked_list.find_all(test_val)
		self.assertEqual(output_arr, [])

	def test_find_all_random(self):
		for i in range(1000):
			nodes_arr = [Node(randint(-10,+10)) for j in range(randint(0,100))]
			if len(nodes_arr) > 0:
				test_val = choice(nodes_arr).value
			else:
				test_val = 100
			linked_list = linked_list_2_by_nodes_arr(nodes_arr)
			output_arr = linked_list.find_all(test_val)
			ans_arr = [x for x in nodes_arr if x.value == test_val]
			self.assertEqual(output_arr, ans_arr)

	def test_single_deletion_regression(self):
		linked_list = linked_list_2_by_values_arr([1,2,3,4,5])
		linked_list.delete(3)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1,2,4,5])

	def test_single_deletion_first_elem(self):
		linked_list = linked_list_2_by_values_arr([1,2,3,4,5])
		linked_list.delete(1)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [2,3,4,5])

	def test_single_deletion_last_elem(self):
		linked_list = linked_list_2_by_values_arr([1,2,3,4,5])
		linked_list.delete(5)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1,2,3,4])

	def test_single_deletion_with_empty_result(self):
		linked_list = linked_list_2_by_values_arr([1])
		linked_list.delete(1)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [])

	def test_single_deletion_first_elem_with_single_elem_result(self):
		linked_list = linked_list_2_by_values_arr([1,2])
		linked_list.delete(1)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [2])

	def test_single_deletion_last_elem_with_single_elem_result(self):
		linked_list = linked_list_2_by_values_arr([1,2])
		linked_list.delete(2)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1])

	def test_single_deletion_random(self):
		for i in range(1000):
			values_arr = [randint(-10,+10) for j in range(randint(1,100))]
			test_val = choice(values_arr)
			linked_list = linked_list_2_by_values_arr(values_arr)
			linked_list.delete(test_val)
			values_arr.remove(test_val)
			self.assertTrue(check_linked_list_2_correct(linked_list))
			self.assertEqual([x.value for x in linked_list], values_arr)

	def test_multiple_deletion_regression(self):
		linked_list = linked_list_2_by_values_arr([1,2,3,3,3,4,5])
		linked_list.delete(3, all=True)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [1,2,4,5])

	def test_multiple_deletion_with_empty_result(self):
		linked_list = linked_list_2_by_values_arr([1,1,1,1,1,1])
		linked_list.delete(1, all=True)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [])

	def test_multiple_deletion_random(self):
		for i in range(1000):
			values_arr = [randint(-5,+5) for j in range(randint(1,100))]
			test_val = choice(values_arr)
			linked_list = linked_list_2_by_values_arr(values_arr)
			linked_list.delete(test_val, all=True)
			ans_arr = [x for x in values_arr if x != test_val]
			self.assertTrue(check_linked_list_2_correct(linked_list))
			self.assertEqual([x.value for x in linked_list], ans_arr)

	def test_insert_regression(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2])
		linked_list.insert(node1, node3)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1, node3, node2])

	def test_insert_last_elem(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2])
		linked_list.insert(node2, node3)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1, node2, node3])

	def test_insert_with_afterNode_None_and_empty_list(self):
		node1 = Node(1)
		linked_list = LinkedList2()
		linked_list.insert(None, node1)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1])

	def test_insert_with_afterNode_None_and_no_empty_list(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node1, node2])
		linked_list.insert(None, node3)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1, node2, node3])

	def test_insert_random(self):
		for i in range(1000):
			nodes_arr = [Node(randint(-10,+10)) for j in range(randint(0,100))]
			linked_list = linked_list_2_by_nodes_arr(nodes_arr)
			after_node = choice(nodes_arr + [None])
			test_node = Node(100)
			linked_list.insert(after_node, test_node)
			if after_node is None:
				nodes_arr.append(test_node)
			else:
				nodes_arr.insert(nodes_arr.index(after_node) + 1, test_node)
			self.assertTrue(check_linked_list_2_correct(linked_list))
			self.assertEqual([x for x in linked_list], nodes_arr)

	def test_add_in_head_regression(self):
		node1, node2, node3 = (Node(x) for x in [1,2,3])
		linked_list = linked_list_2_by_nodes_arr([node2, node3])
		linked_list.add_in_head(node1)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1, node2, node3])

	def test_add_in_head_of_empty_list(self):
		node1 = Node(1)
		linked_list = LinkedList2()
		linked_list.add_in_head(node1)
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x for x in linked_list], [node1])

	def test_add_in_head_random(self):
		for i in range(1000):
			nodes_arr = [Node(randint(-10,+10)) for j in range(randint(0,100))]
			linked_list = linked_list_2_by_nodes_arr(nodes_arr)
			test_node = Node(100)
			linked_list.add_in_head(test_node)
			self.assertTrue(check_linked_list_2_correct(linked_list))
			self.assertEqual([x for x in linked_list], [test_node] + nodes_arr)

	def test_clean_regression(self):
		linked_list = linked_list_2_by_values_arr([1,2,3,4,5])
		linked_list.clean()
		self.assertTrue(check_linked_list_2_correct(linked_list))
		self.assertEqual([x.value for x in linked_list], [])

	def test_len_regression(self):
		linked_list = linked_list_2_by_values_arr([1,2,3,4,5])
		self.assertEqual(linked_list.len(), 5)

	def test_len_of_empty_list(self):
		linked_list = LinkedList2()
		self.assertEqual(linked_list.len(), 0)

	def test_len_random(self):
		for i in range(1000):
			values_arr = [randint(-10,+10) for j in range(randint(0,100))]
			linked_list = linked_list_2_by_values_arr(values_arr)
			self.assertEqual(linked_list.len(), len(values_arr))

if __name__ == '__main__':
	unittest.main()