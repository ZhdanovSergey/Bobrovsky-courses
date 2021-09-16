class Queue:
  def __init__(self):
    self._store = []

  def enqueue(self, item):
    self._store.insert(0, item)

  def dequeue(self):
    if self.size() > 0:
    	return self._store.pop()
    else:
    	return None

  def size(self):
    return len(self._store)