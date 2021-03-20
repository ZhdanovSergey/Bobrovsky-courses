class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedListIterator:

    def __init__(self, linked_list):
        self.current_node = linked_list.head

    def __next__(self):
        node = self.current_node
        if node is not None:
            self.current_node = self.current_node.next
            return node
        else:
            raise StopIteration

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        return LinkedListIterator(self)

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        arr = []
        node = self.head
        while node is not None:
            if node.value == val:
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                if node is self.head:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if node is self.tail:
                    self.tail = prev_node
                if not all:
                    break
            else:
                prev_node = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            cut_end = self.head
            self.head = newNode
        else:
            cut_start = afterNode
            cut_end = afterNode.next
            cut_start.next = newNode
        newNode.next = cut_end
        if self.tail is afterNode:
            self.tail = newNode
