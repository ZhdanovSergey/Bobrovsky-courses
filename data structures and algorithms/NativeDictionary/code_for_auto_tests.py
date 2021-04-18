class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 3

    def hash_fun(self, key):
        return sum([ord(x) for x in key]) % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        while True:
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                break
            elif self.slots[index] == key:
                self.values[index] = value
                break
            index = (index + self.step) % self.size

    def get(self, key):
        if self.is_key(key):
            index = self.slots.index(key)
            return self.values[index]
        else:
            return None