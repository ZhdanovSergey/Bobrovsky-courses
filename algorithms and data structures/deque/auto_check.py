class Deque:
    def __init__(self):
        self._store = []

    def addFront(self, item):
        self._store.insert(0, item)

    def addTail(self, item):
        self._store.append(item)

    def removeFront(self):
        if self.size() > 0:
            return self._store.pop(0)
        return None

    def removeTail(self):
        if self.size() > 0:
            return self._store.pop()
        return None

    def size(self):
        return len(self._store)