import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __iter__(self):
        return self._generator()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def __len__(self):
        return self.count

    def _generator(self):
        current = 0
        while current < self.count:
            yield self[current]
            current += 1

    def _increase_capacity_if_necessary(self):
        if self.count + 1 > self.capacity:
            self.resize(2*self.capacity)

    def _reduce_capacity_if_necessary(self):
        min_capacity = 16
        if self.count - 1 < self.capacity/2 and self.capacity > min_capacity:
            self.resize(max(int(self.capacity / 1.5), min_capacity))

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        self._increase_capacity_if_necessary()
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i > self.count:
            raise IndexError
        self._increase_capacity_if_necessary()
        for j in range(self.count, i, -1):
            self.array[j] = self.array[j-1]
        self.array[i] = itm
        self.count += 1


    def delete(self, i):
        if i >= self.count:
            raise IndexError
        self._reduce_capacity_if_necessary()
        for j in range(i, self.count-1):
            self.array[j] = self.array[j+1]
        self.count -= 1