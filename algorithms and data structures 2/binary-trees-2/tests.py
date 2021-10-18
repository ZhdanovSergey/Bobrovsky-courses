import unittest
import random
from code import aBST


class aBSTTests(unittest.TestCase):
	def getTestTree(self):
		tree = aBST(3)
		tree.Tree = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]
		return tree

	def test_FindKeyIndexEmptyTree(self):
		tree = aBST(-1)
		result = tree.FindKeyIndex(1)
		self.assertTrue(result is None)

	def test_FindKeyIndexOneLevelSuccess(self):
		tree = aBST(0)
		testKey = 1
		tree.Tree[0] = testKey
		result = tree.FindKeyIndex(testKey)
		self.assertEqual(result, 0)

	def test_FindKeyIndexOneLevelEmpty(self):
		tree = aBST(0)
		result = tree.FindKeyIndex(1)
		self.assertEqual(result, 0)

	def test_FindKeyIndexOneLevelUnsuccess(self):
		tree = aBST(0)
		tree.Tree[0] = 1
		result = tree.FindKeyIndex(2)
		self.assertTrue(result is None)

	def test_FindKeyIndexSuccess(self):
		tree = self.getTestTree()
		result = tree.FindKeyIndex(62)
		self.assertEqual(result, 5)

	def test_FindKeyIndexSuccessRoot(self):
		tree = self.getTestTree()
		result = tree.FindKeyIndex(50)
		self.assertEqual(result, 0)

	def test_FindKeyIndexSuccessLeaf(self):
		tree = self.getTestTree()
		result = tree.FindKeyIndex(43)
		self.assertEqual(result, 10)

	def test_FindKeyIndexEmptyCell(self):
		tree = self.getTestTree()
		result = tree.FindKeyIndex(24)
		self.assertEqual(result, -3)

	def test_FindKeyIndexOutOfTree(self):
		tree = self.getTestTree()
		result = tree.FindKeyIndex(54)
		self.assertEqual(result, None)

	def test_AddKeyEmptyTree(self):
		tree = aBST(-1)
		result = tree.AddKey(1)
		self.assertEqual(result, -1)

	def test_AddKeyOneLevelSuccess(self):
		tree = aBST(0)
		result = tree.AddKey(1)
		self.assertEqual(result, 0)

	def test_AddKeyOneLevelAlreadyExist(self):
		tree = aBST(0)
		tree.Tree[0] = 0
		result = tree.AddKey(0)
		self.assertEqual(result, -1)

	def test_AddKeyOneLevelOutOfTree(self):
		tree = aBST(0)
		tree.Tree[0] = 0
		result = tree.AddKey(1)
		self.assertEqual(result, -1)

	def test_AddKeySuccess(self):
		tree = self.getTestTree()
		result = tree.AddKey(24)
		self.assertEqual(result, 3)

	def test_AddKeyAlreadyExist(self):
		tree = self.getTestTree()
		result = tree.AddKey(62)
		self.assertEqual(result, -1)

	def test_AddKeyAlreadyExistLeaf(self):
		tree = self.getTestTree()
		result = tree.AddKey(92)
		self.assertEqual(result, -1)

	def test_AddKeyOutOfTree(self):
		tree = self.getTestTree()
		result = tree.AddKey(45)
		self.assertEqual(result, -1)

if __name__ == '__main__':
	unittest.main()