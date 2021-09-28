import unittest
from code import BSTNode, BSTFind, BST


class BSTTests(unittest.TestCase):
	def test_FindNodeByKey(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		self.assertTrue(tree.FindNodeByKey(1).Node is node)

	def test_AddKeyValue(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		tree.AddKeyValue(2, 2)

	def test_FinMinMax(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		tree.FinMinMax(node, True)

	def test_DeleteNodeByKey(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		tree.DeleteNodeByKey(1)

	def test_Count(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		self.assertEqual(tree.Count(), 1)

	def test_CountEmpty(self):
		tree = BST(None)
		self.assertEqual(tree.Count(), 0)

if __name__ == '__main__':
	unittest.main()