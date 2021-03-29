class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        return self._generator()

    def _generator(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

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
        for node in self:
            if node.value == val:
                return node
        return None

    def find_all(self, val):
        return [node for node in self if node.value == val]

    def clean(self):
        self.head = None
        self.tail = None

    def delete(self, val, all=False):
        for node in self:
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

    def len(self):
        count = 0
        for node in self: count += 1
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