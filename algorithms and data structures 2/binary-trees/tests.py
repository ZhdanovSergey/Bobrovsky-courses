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


	def test_FindNodeByKeyEmpty(self):
		tree = BST(None)
		result = tree.FindNodeByKey(0)
		self.assertTrue(result.Node is None)

	def test_FindNodeByKeyOneNode(self):
		testKey = 0
		node = BSTNode(testKey, testKey, None)
		tree = BST(node)
		result = tree.FindNodeByKey(testKey)
		self.assertTrue(result.Node is node)
		self.assertTrue(result.NodeHasKey is True)

	def test_FindNodeByKeyExisting(self):
		(tree, nodes) = self.getTestTree()
		result = tree.FindNodeByKey(3)
		self.assertTrue(result.Node is nodes[3])
		self.assertTrue(result.NodeHasKey is True)

	def test_FindNodeByKeyNotExistingLeft(self):
		(tree, nodes) = self.getTestTree()
		result = tree.FindNodeByKey(-1)
		self.assertTrue(result.Node is nodes[0])
		self.assertTrue(result.NodeHasKey is False)
		self.assertTrue(result.ToLeft is True)

	def test_FindNodeByKeyNotExistingRight(self):
		(tree, nodes) = self.getTestTree()
		result = tree.FindNodeByKey(15)
		self.assertTrue(result.Node is nodes[14])
		self.assertTrue(result.NodeHasKey is False)
		self.assertTrue(result.ToLeft is False)

	def test_AddKeyValueToEmptyTree(self):
		tree = BST(None)
		testKey = 1
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.AddKeyValue(testKey, testKey)
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)

	def test_AddKeyValueToLeft(self):
		(tree, nodes) = self.getTestTree()
		testKey = -1
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.AddKeyValue(testKey, testKey)
		findResult = tree.FindNodeByKey(testKey)
		self.assertTrue(findResult.NodeHasKey)
		self.assertTrue(nodes[0].LeftChild is findResult.Node)

	def test_AddKeyValueToRight(self):
		(tree, nodes) = self.getTestTree()
		testKey = 15
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.AddKeyValue(testKey, testKey)
		findResult = tree.FindNodeByKey(testKey)
		self.assertTrue(findResult.NodeHasKey)
		self.assertTrue(nodes[14].RightChild is findResult.Node)

	def test_AddKeyValueAlreadyExisting(self):
		(tree, nodes) = self.getTestTree()
		testKey = 9
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertFalse(tree.AddKeyValue(testKey, testKey))

	def test_FinMinMaxFromRootMin(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes[7], False) is nodes[0])

	def test_FinMinMaxFromRootMax(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes[7], True) is nodes[14])

	def test_FinMinMaxFromSubtreeMin(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes[11], False) is nodes[8])

	def test_FinMinMaxFromSubtreeMax(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes[3], True) is nodes[6])

	def test_DeleteNodeByKeyNotExisting(self):
		(tree, nodes) = self.getTestTree()
		self.assertFalse(tree.DeleteNodeByKey(-1))

	def test_DeleteNodeByKeyEmpty(self):
		tree = BST(None)
		self.assertFalse(tree.DeleteNodeByKey(0))

	def test_DeleteNodeByKeyOneNode(self):
		testKey = 0
		tree = BST(BSTNode(testKey, testKey, None))
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(tree.Root is None)

	def test_DeleteNodeByKeyWithNoChild(self):
		(tree, nodes) = self.getTestTree()
		testKey = 4
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes[5].LeftChild is None)

	def test_DeleteNodeByKeyWithOnlyLeftChild(self):
		(tree, nodes) = self.getTestTree()
		testKey = 3
		nodes[testKey].RightChild = None
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes[7].LeftChild is nodes[1])
		self.assertTrue(nodes[1].Parent is nodes[7])

	def test_DeleteNodeByKeyWithOnlyRightChild(self):
		(tree, nodes) = self.getTestTree()
		testKey = 11
		nodes[testKey].LeftChild = None
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes[7].RightChild is nodes[13])
		self.assertTrue(nodes[13].Parent is nodes[7])

	def test_DeleteNodeByKeyWithBothChild(self):
		(tree, nodes) = self.getTestTree()
		testKey = 3
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes[7].LeftChild is nodes[4])
		self.assertTrue(nodes[4].Parent is nodes[7])
		self.assertTrue(nodes[4].LeftChild is nodes[1])
		self.assertTrue(nodes[4].RightChild is nodes[5])
		self.assertTrue(nodes[1].Parent is nodes[4])
		self.assertTrue(nodes[5].Parent is nodes[4])
		self.assertTrue(nodes[5].LeftChild is None)

	def test_DeleteNodeByKeyRandom(self):
		for _ in range(10000):
			(tree, nodes) = self.getTestTree()
			deletedKeys = []

			while len(nodes):
				testNode = random.choice(nodes)
				testKey = testNode.NodeKey
				deletedKeys.append(testKey)
				self.assertTrue(testNode in nodes)
				self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey, deletedKeys)
				nodes.remove(testNode)
				tree.DeleteNodeByKey(testKey)
				self.assertFalse(testNode in nodes)
				self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)

	def test_DeleteNodeByKeyCase_7_10(self):
		(tree, nodes) = self.getTestTree()
		nodes[9].LeftChild = None
		keyToDelete = 7
		problemKey = 10

		self.assertTrue(tree.FindNodeByKey(keyToDelete).NodeHasKey)
		self.assertTrue(tree.FindNodeByKey(problemKey).NodeHasKey)
		tree.DeleteNodeByKey(keyToDelete)
		self.assertFalse(tree.FindNodeByKey(keyToDelete).NodeHasKey)
		self.assertTrue(tree.FindNodeByKey(problemKey).NodeHasKey)

	def test_DeleteNodeByKeyLastNode(self):
		(tree, nodes) = self.getTestTree()
		testKey = 14
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes[13].RightChild is None)

	def test_CountEmpty(self):
		tree = BST(None)
		self.assertEqual(tree.Count(), 0)

	def test_CountOneNode(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		self.assertEqual(tree.Count(), 1)

	def test_Count(self):
		(tree, nodes) = self.getTestTree()
		self.assertEqual(tree.Count(), len(nodes))

if __name__ == '__main__':
	unittest.main()