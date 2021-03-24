class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2Iterator:

    def __init__(self, linked_list):
        self.current_node = linked_list.head

    def __next__(self):
        node = self.current_node
        if node is not None:
            self.current_node = self.current_node.next
            return node
        else:
            raise StopIteration

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        return LinkedList2Iterator(self)

    def add_in_head(self, item):
        if self.head is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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

    def clean(self):
        self.head = None
        self.tail = None

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if (node is not self.head) and (node is not self.tail):
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:
                    if self.head is self.tail:
                        self.clean()
                    elif node is self.head:
                        self.head = node.next
                        self.head.prev = None
                    else:
                        self.tail = node.prev
                        self.tail.next = None
                if not all:
                    break
            node = node.next

    def len(self):
        count = 0
        for x in self:
            count += 1
        return count

    def insert(self, afterNode, newNode):
        if (afterNode is None) or (afterNode is self.tail):
            self.add_in_tail(newNode)
        else:
            cut_start = afterNode
            cut_end = afterNode.next
            cut_start.next = newNode
            cut_end.prev = newNode
            newNode.prev = cut_start
            newNode.next = cut_end