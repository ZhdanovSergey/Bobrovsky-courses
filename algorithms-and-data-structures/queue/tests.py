import unittest
from auto_check import Queue
from queue_by_two_stacks import Queue_by_stacks
from rotate_func import rotate_queue

class QueueTests(unittest.TestCase):

	def create_queue_from_array(self, arr):
		queue = Queue()
		queue._store = arr
		return queue

	def test_size(self):
		queue = self.create_queue_from_array([1,2,3])
		self.assertEqual(queue.size(), 3)

	def test_size_of_empty_queue(self):
		queue = self.create_queue_from_array([])
		self.assertEqual(queue.size(), 0)

	def test_enqueue(self):
		queue = self.create_queue_from_array([1,2,3])
		queue.enqueue(4)
		self.assertEqual(queue._store, [4,1,2,3])

	def test_enqueue_empty_queue(self):
		queue = self.create_queue_from_array([])
		queue.enqueue(1)
		self.assertEqual(queue._store, [1])

	def test_dequeue(self):
		queue = self.create_queue_from_array([1,2,3])
		dequeue_result = queue.dequeue()
		self.assertEqual(dequeue_result, 3)
		self.assertEqual(queue._store, [1,2])

	def test_dequeue_empty_queue(self):
		queue = self.create_queue_from_array([])
		dequeue_result = queue.dequeue()
		self.assertEqual(dequeue_result, None)
		self.assertEqual(queue._store, [])

	def test_rotate_func(self):
		queue = self.create_queue_from_array([1,2,3])
		queue = rotate_queue(queue, 2)
		self.assertEqual(queue._store, [2,3,1])

	def test_rotate_func_empty_queue(self):
		queue = self.create_queue_from_array([])
		queue = rotate_queue(queue, 2)
		self.assertEqual(queue._store, [])

	def create_queue_by_stacks_from_array(self, arr):
		queue = Queue_by_stacks()
		queue._store._store = arr
		return queue

	def test_size(self):
		queue = self.create_queue_by_stacks_from_array([1,2,3])
		self.assertEqual(queue.size(), 3)

	def test_size_of_empty_queue(self):
		queue = self.create_queue_by_stacks_from_array([])
		self.assertEqual(queue.size(), 0)

	def test_enqueue(self):
		queue = self.create_queue_by_stacks_from_array([1,2,3])
		queue.enqueue(4)
		self.assertEqual(queue._store._store, [4,1,2,3])

	def test_enqueue_empty_queue(self):
		queue = self.create_queue_by_stacks_from_array([])
		queue.enqueue(1)
		self.assertEqual(queue._store._store, [1])

	def test_dequeue(self):
		queue = self.create_queue_by_stacks_from_array([1,2,3])
		dequeue_result = queue.dequeue()
		self.assertEqual(dequeue_result, 3)
		self.assertEqual(queue._store._store, [1,2])

	def test_dequeue_empty_queue(self):
		queue = self.create_queue_by_stacks_from_array([])
		dequeue_result = queue.dequeue()
		self.assertEqual(dequeue_result, None)
		self.assertEqual(queue._store._store, [])

if __name__ == '__main__':
	unittest.main()