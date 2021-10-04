import unittest
import random
from code import BSTNode, BSTFind, BST


class BSTTests(unittest.TestCase):
	def getTestTree(self):
		nodes = []

		for i in range(15):
			nodes.append(BSTNode(i, i, None))

		nodes[1].LeftChild = nodes[0]
		nodes[1].RightChild = nodes[2]
		nodes[0].Parent = nodes[1]
		nodes[2].Parent = nodes[1]

		nodes[5].LeftChild = nodes[4]
		nodes[5].RightChild = nodes[6]
		nodes[4].Parent = nodes[5]
		nodes[6].Parent = nodes[5]

		nodes[3].LeftChild = nodes[1]
		nodes[3].RightChild = nodes[5]
		nodes[1].Parent = nodes[3]
		nodes[5].Parent = nodes[3]

		nodes[9].LeftChild = nodes[8]
		nodes[9].RightChild = nodes[10]
		nodes[8].Parent = nodes[9]
		nodes[10].Parent = nodes[9]

		nodes[13].LeftChild = nodes[12]
		nodes[13].RightChild = nodes[14]
		nodes[12].Parent = nodes[13]
		nodes[14].Parent = nodes[13]

		nodes[11].LeftChild = nodes[9]
		nodes[11].RightChild = nodes[13]
		nodes[9].Parent = nodes[11]
		nodes[13].Parent = nodes[11]

		nodes[7].LeftChild = nodes[3]
		nodes[7].RightChild = nodes[11]
		nodes[3].Parent = nodes[7]
		nodes[11].Parent = nodes[7]

		tree = BST(nodes[7])

		return (tree, nodes)

	def test_WideAllNodesEmpty(self):
		tree = BST(None)
		result = tree.WideAllNodes()
		correct_answer = tuple()
		self.assertEqual(result, correct_answer)

	def test_WideAllNodesOneNode(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		result = tree.WideAllNodes()
		correct_answer = tuple([node])
		self.assertEqual(result, correct_answer)

	def test_WideAllNodesFullTree(self):
		(tree, nodes) = self.getTestTree()
		result = tree.WideAllNodes()
		correct_answer = tuple(nodes[x] for x in (7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14))
		self.assertEqual(result, correct_answer)

	def test_WideAllNodesNotFullTree(self):
		(tree, nodes) = self.getTestTree()
		nodes[11].LeftChild = None
		nodes[11].RightChild = None
		result = tree.WideAllNodes()
		correct_answer = tuple(nodes[x] for x in (7, 3, 11, 1, 5, 0, 2, 4, 6))
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesEmptyIn(self):
		tree = BST(None)
		result = tree.DeepAllNodes(0)
		correct_answer = tuple()
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesEmptyPost(self):
		tree = BST(None)
		result = tree.DeepAllNodes(1)
		correct_answer = tuple()
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesEmptyPre(self):
		tree = BST(None)
		result = tree.DeepAllNodes(2)
		correct_answer = tuple()
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesOneNodeIn(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		result = tree.DeepAllNodes(0)
		correct_answer = tuple([node])
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesOneNodePost(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		result = tree.DeepAllNodes(1)
		correct_answer = tuple([node])
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesOneNodePre(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		result = tree.DeepAllNodes(2)
		correct_answer = tuple([node])
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesFullTreeIn(self):
		(tree, nodes) = self.getTestTree()
		result = tree.DeepAllNodes(0)
		correct_answer = tuple(nodes[x] for x in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesFullTreePost(self):
		(tree, nodes) = self.getTestTree()
		result = tree.DeepAllNodes(1)
		correct_answer = tuple(nodes[x] for x in (0, 2, 1, 4, 6, 5, 3, 8, 10, 9, 12, 14, 13, 11, 7))
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesFullTreePre(self):
		(tree, nodes) = self.getTestTree()
		result = tree.DeepAllNodes(2)
		correct_answer = tuple(nodes[x] for x in (7, 3, 1, 0, 2, 5, 4, 6, 11, 9, 8, 10, 13, 12, 14))
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesNotFullTreeIn(self):
		(tree, nodes) = self.getTestTree()
		nodes[11].LeftChild = None
		nodes[11].RightChild = None
		result = tree.DeepAllNodes(0)
		correct_answer = tuple(nodes[x] for x in (0, 1, 2, 3, 4, 5, 6, 7, 11))
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesNotFullTreePost(self):
		(tree, nodes) = self.getTestTree()
		nodes[11].LeftChild = None
		nodes[11].RightChild = None
		result = tree.DeepAllNodes(1)
		correct_answer = tuple(nodes[x] for x in (0, 2, 1, 4, 6, 5, 3, 11, 7))
		self.assertEqual(result, correct_answer)

	def test_DeepAllNodesNotFullTreePre(self):
		(tree, nodes) = self.getTestTree()
		nodes[11].LeftChild = None
		nodes[11].RightChild = None
		result = tree.DeepAllNodes(2)
		correct_answer = tuple(nodes[x] for x in (7, 3, 1, 0, 2, 5, 4, 6, 11))
		self.assertEqual(result, correct_answer)

if __name__ == '__main__':
	unittest.main()