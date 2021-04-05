import unittest
from auto_check import Deque
from palindrome_func import check_palindrome

class QueueTests(unittest.TestCase):

	def create_deque_from_array(self, arr):
		queue = Deque()
		queue._store = arr
		return queue

	def test_size(self):
		queue = self.create_deque_from_array([1,2,3])
		self.assertEqual(queue.size(), 3)

	def test_size_empty(self):
		queue = self.create_deque_from_array([])
		self.assertEqual(queue.size(), 0)

	def test_addFront(self):
		queue = self.create_deque_from_array([1,2,3])
		queue.addFront(4)
		self.assertEqual(queue._store, [4,1,2,3])

	def test_addFront_empty(self):
		queue = self.create_deque_from_array([])
		queue.addFront(4)
		self.assertEqual(queue._store, [4])

	def test_addTail(self):
		queue = self.create_deque_from_array([1,2,3])
		queue.addTail(4)
		self.assertEqual(queue._store, [1,2,3,4])

	def test_addTail_empty(self):
		queue = self.create_deque_from_array([])
		queue.addTail(4)
		self.assertEqual(queue._store, [4])

	def test_removeFront(self):
		queue = self.create_deque_from_array([1,2,3])
		output = queue.removeFront()
		self.assertEqual(queue._store, [2,3])
		self.assertEqual(output, 1)

	def test_removeFront_empty(self):
		queue = self.create_deque_from_array([])
		output = queue.removeFront()
		self.assertEqual(queue._store, [])
		self.assertEqual(output, None)

	def test_removeTail(self):
		queue = self.create_deque_from_array([1,2,3])
		output = queue.removeTail()
		self.assertEqual(queue._store, [1,2])
		self.assertEqual(output, 3)

	def test_removeTail_empty(self):
		queue = self.create_deque_from_array([])
		output = queue.removeTail()
		self.assertEqual(queue._store, [])
		self.assertEqual(output, None)

	def test_palindrome_func(self):
		self.assertTrue(check_palindrome('qweewq'))
		self.assertTrue(check_palindrome('qwewq'))
		self.assertFalse(check_palindrome('qweewqq'))
		self.assertTrue(check_palindrome('q'))
		self.assertTrue(check_palindrome(''))

if __name__ == '__main__':
	unittest.main()