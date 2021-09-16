class Stack:
    def __init__(self):
        self._store = []

    def size(self):
        return len(self._store)

    def pop(self):
        if self.size() > 0:
            return self._store.pop()
        return None

    def push(self, value):
        self._store.append(value)

    def peek(self):
        if self.size() > 0:
            return self._store[-1]
        return None