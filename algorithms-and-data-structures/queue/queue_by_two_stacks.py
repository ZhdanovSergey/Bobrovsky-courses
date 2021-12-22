import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from stack.auto_check_tail import Stack

class Queue_by_stacks():
  def __init__(self):
    self._store = Stack()

  def _create_reverse_stack(self, stack):
    reverse_stack = Stack()
    for i in range(stack.size()):
      reverse_stack.push(stack.pop())
    return reverse_stack

  def enqueue(self, item):
    reverse_stack = self._create_reverse_stack(self._store)
    reverse_stack.push(item)
    self._store = self._create_reverse_stack(reverse_stack)

  def dequeue(self):
    return self._store.pop()

  def size(self):
    return self._store.size()