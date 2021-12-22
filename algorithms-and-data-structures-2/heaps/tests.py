import math
import random
import unittest

from code import Heap


class HeapTests(unittest.TestCase):
	def getHeap(self, arr, depth):
		heap = Heap()
		heap.MakeHeap(arr, depth)
		return heap

	def test_AddSuccess(self):
		heap = self.getHeap([2, 1], 1)
		self.assertTrue(heap.Add(3))

	def test_AddError(self):
		heap = self.getHeap([2, 1, 3], 1)
		self.assertFalse(heap.Add(10))

	def test_MakeHeapEmpty(self):
		heap = self.getHeap([], 0)
		self.assertTrue(heap.HeapArray == [None])

	def test_MakeHeapEmptyOneKey(self):
		heap = self.getHeap([1], 0)
		self.assertTrue(heap.HeapArray == [1])

	def test_MakeHeapEmptyTwoKeys(self):
		heap = self.getHeap([2, 1], 1)
		self.assertTrue(heap.HeapArray == [2, 1, None])

	def test_MakeHeapEmptyThreeKeys(self):
		heap = self.getHeap([2, 1, 3], 1)
		self.assertTrue(heap.HeapArray == [3, 1, 2])

	def test_MakeHeapEmptyFourKeys(self):
		heap = self.getHeap([2, 1, 3, 4], 2)
		self.assertTrue(heap.HeapArray == [4, 3, 2, 1, None, None, None])

	def test_GetMaxEmpty(self):
		heap = self.getHeap([], 0)
		result = heap.GetMax()
		self.assertTrue(result, -1)
		self.assertTrue(heap.HeapArray == [None])

	def test_GetMaxOneNode(self):
		heap = self.getHeap([1], 0)
		result = heap.GetMax()
		self.assertTrue(result, 1)
		self.assertTrue(heap.HeapArray == [None])

	def test_GetMaxTwoNodes(self):
		heap = self.getHeap([2, 1], 1)
		result = heap.GetMax()
		self.assertTrue(result, 2)
		self.assertTrue(heap.HeapArray == [1, None, None])

	def test_GetMaxThreeNodes(self):
		heap = self.getHeap([2, 1, 3], 1)
		result = heap.GetMax()
		self.assertTrue(result, 3)
		self.assertTrue(heap.HeapArray == [2, 1, None])

	def test_GetMaxFourNodes(self):
		heap = self.getHeap([2, 1, 3, 4], 2)
		result = heap.GetMax()
		self.assertTrue(result, 4)
		self.assertTrue(heap.HeapArray == [3, 1, 2, None, None, None, None])

if __name__ == '__main__':
	unittest.main()