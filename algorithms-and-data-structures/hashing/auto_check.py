class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum([ord(x) for x in value]) % self.size

    def seek_slot(self, value):
        init_index = self.hash_fun(value)
        index = init_index
        while True:
            if self.slots[index] is None:
                return index
            else:
                index = (index + self.step) % self.size
            if index == init_index:
                return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None
            

    def find(self, value):
        init_index = self.hash_fun(value)
        index = init_index
        while True:
            if self.slots[index] == value:
                return index
            elif self.slots[index] is None:
                return None
            else:
                index = (index + self.step) % self.size
            if index == init_index:
                return None