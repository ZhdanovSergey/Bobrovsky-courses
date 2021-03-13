from exercise_1_6 import Node, LinkedList


print('delete test\n')
arr = [1,3,4,2,1]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

linked_list.delete(1)
linked_list.print_all_nodes()
print()
linked_list.delete(2)
linked_list.print_all_nodes()
print()
linked_list.delete(3)
linked_list.print_all_nodes()


print('multiple delete test\n')
arr = [1,1,2,2]
linked_list = LinkedList()
for x in arr:
	linked_list.add_in_tail(Node(x))

linked_list.print_all_nodes()
print()

linked_list.delete(2, all=True)
linked_list.print_all_nodes()


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
print()

linked_list.insert(None, Node(6))
linked_list.print_all_nodes()


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