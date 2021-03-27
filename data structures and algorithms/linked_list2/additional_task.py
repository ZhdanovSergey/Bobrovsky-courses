class DummyNode:
    def __init__(self):
        self.prev = None
        self.next = None

class Node(DummyNode):
    def __init__(self, v):
        super().__init__()
        self.value = v

class LinkedList2Iterator:

    def __init__(self, linked_list):
        self.current = linked_list.head

    def __next__(self):
        node = self.current
        if isinstance(node, Node):
            self.current = self.current.next
            return node
        else:
            raise StopIteration

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self._dummy = DummyNode()

    def __iter__(self):
        return LinkedList2Iterator(self)

    def add_in_head(self, item):
        if self.head is None:
            self.tail = item
            self.tail.next = self._dummy
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item
        self.head.prev = self._dummy

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.head.prev = self._dummy
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.tail.next = self._dummy

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
                node.prev.next = node.next
                node.next.prev = node.prev
                if self.head is self.tail:
                    self.clean()
                elif node is self.head:
                    self.head = self.head.next
                elif node is self.tail:
                    self.tail = self.tail.prev
                if not all:
                    break

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