from linked_list import Node, LinkedList

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(2)

s_list = LinkedList()
s_list.add_in_tail(a)
s_list.add_in_tail(b)
s_list.add_in_tail(c)
s_list.add_in_tail(d)

s_list.print_all_nodes()
print()

s_list.delete(2, all=True)

s_list.print_all_nodes()