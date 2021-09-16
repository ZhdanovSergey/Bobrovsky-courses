class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def __iter__(self):
        return self._generator()

    def _generator(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return +1
        else:
            return 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif (self.__ascending == (self.compare(new_node.value, self.head.value) < 0)):
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif (self.__ascending == (self.compare(new_node.value, self.tail.value) >= 0)):
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            for node in self:
                if (self.__ascending \
                        and self.compare(new_node.value, node.value) >= 0 \
                        and self.compare(new_node.value, node.next.value) <= 0) \
                    or (not self.__ascending \
                        and self.compare(new_node.value, node.value) <= 0 \
                        and self.compare(new_node.value, node.next.value) >= 0):
                    cut_start = node
                    cut_end = node.next
                    cut_start.next = new_node
                    cut_end.prev = new_node
                    new_node.prev = cut_start
                    new_node.next = cut_end
                    break

    def find(self, val):
        for node in self:
            if node.value == val:
                return node
            if self.__ascending == (self.compare(node.value, val) > 0):
                return None
        return None

    def delete(self, val):
        if self.head is not None:
            if self.head == self.tail:
                if self.head.value == val:
                    self.clean(self.__ascending)
            elif self.head.value == val:
                self.head = self.head.next
                self.head.prev = None
            elif self.tail.value == val:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                for node in self:
                    if node.value == val:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        break


    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc        

    def len(self):
        count = 0
        for node in self:
            count += 1
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        return super().compare(v1.strip(), v2.strip())