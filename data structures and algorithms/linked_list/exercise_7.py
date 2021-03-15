from exercise_1_6 import Node, LinkedList
from exercise_8 import get_sum_of_lists


print('single delete test\n')
arr = [1,3,4,2,1]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

linked_list.delete(1)
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))
print()
linked_list.delete(2)
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))
print()
linked_list.delete(3)
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))
print()
linked_list.delete(1)
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))


print('multiple delete test\n')
arr = [1,1,2,2]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

linked_list.delete(2, all=True)
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))


print('delete single element from 2-elem list\n')
linked_list = LinkedList()
linked_list.add_in_tail(Node(1))
linked_list.add_in_tail(Node(2))

linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))
print()

linked_list.delete(1)
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))


print('test tail content after delete\n')
arr = [1,2,3,4,4]
nodes_arr = []
linked_list = LinkedList()
for x in arr:
	node = Node(x)
	nodes_arr.append(node)
	linked_list.add_in_tail(node)

linked_list.print_all_nodes()
print()

linked_list.delete(4, all=True)

linked_list.print_all_nodes()
print()

print(linked_list.tail is nodes_arr[2])


print('clean test\n')
arr = [1,2,3,2]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

linked_list.clean()
linked_list.print_all_nodes()


print('find_all test\n')
arr = [1,2,3,2]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

print(linked_list.find_all(2))


print('len test\n')
arr = [1,2,3,2]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

print(linked_list.len())


print('insert test\n')
arr = [1,2,3]
nodes_arr = []
linked_list = LinkedList()
for x in arr:
	node = Node(x)
	nodes_arr.append(node)
	linked_list.add_in_tail(node)

linked_list.print_all_nodes()
print()

linked_list.insert(nodes_arr[1], Node(5))
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))
print()

linked_list.insert(None, Node(6))
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))
print()

linked_list.insert(nodes_arr[len(nodes_arr) - 1], Node(10))
linked_list.print_all_nodes()
print('head ' + str(linked_list.head.value))
print('tail ' + str(linked_list.tail.value))


print('test tail content after insert\n')
arr = [1,2,3]
a = Node(5)
nodes_arr = []
linked_list = LinkedList()
for x in arr:
	node = Node(x)
	nodes_arr.append(node)
	linked_list.add_in_tail(node)

linked_list.print_all_nodes()
print()

linked_list.insert(nodes_arr[len(arr) - 1], a)
linked_list.print_all_nodes()
print()

print(linked_list.tail is a)


print('sum of lists test')
arr1 = [1,2,3]
arr2 = [8,7,6]
linked_list1 = LinkedList()
linked_list2 = LinkedList()
for x in arr1:
	linked_list1.add_in_tail(Node(x))
for x in arr2:
	linked_list2.add_in_tail(Node(x))

linked_list1.print_all_nodes()
print()
linked_list2.print_all_nodes()
print()
a = get_sum_of_lists(linked_list1, linked_list2)
a.print_all_nodes()