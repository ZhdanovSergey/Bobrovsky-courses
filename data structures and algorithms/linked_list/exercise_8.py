from exercise_1_6 import Node, LinkedList

def get_sum_of_lists(list1, list2):
	if list1.len() == list2.len():
		result_list = LinkedList()
		list1_node = list1.head
		list2_node = list2.head
		while list1_node is not None:
			result_list.add_in_tail(Node(list1_node.value + list2_node.value))
			list1_node = list1_node.next
			list2_node = list2_node.next
		return result_list
	else:
		return None