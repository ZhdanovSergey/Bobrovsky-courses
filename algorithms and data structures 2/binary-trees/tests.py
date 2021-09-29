import unittest
from code import BSTNode, BSTFind, BST


class BSTTests(unittest.TestCase):
	def getTestTree(self):
		node5 = BSTNode(5, 5, None)
		node3 = BSTNode(3, 3, node5)
		node7 = BSTNode(7, 7, node5)
		node5.LeftChild = node3
		node5.RightChild = node7

		node2 = BSTNode(2, 2, node3)
		node4 = BSTNode(4, 4, node3)
		node3.LeftChild = node2
		node3.RightChild = node4

		node6 = BSTNode(6, 6, node7)
		node8 = BSTNode(8, 8, node7)
		node7.LeftChild = node6
		node7.RightChild = node8

		tree = BST(node5)
		return (tree, {
			'2': node2,
			'3': node3,
			'4': node4,
			'5': node5,
			'6': node6,
			'7': node7,
			'8': node8,
		})

	def test_FindNodeByKeyEmpty(self):
		tree = BST(None)
		result = tree.FindNodeByKey(1)
		self.assertTrue(result.Node is None)

	def test_FindNodeByKeyOneNode(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		result = tree.FindNodeByKey(1)
		self.assertTrue(result.Node is node)
		self.assertTrue(result.NodeHasKey is True)

	def test_FindNodeByKeyExisting(self):
		(tree, nodes) = self.getTestTree()
		result = tree.FindNodeByKey(3)
		self.assertTrue(result.Node is nodes['3'])
		self.assertTrue(result.NodeHasKey is True)

	def test_FindNodeByKeyNotExistingLeft(self):
		(tree, nodes) = self.getTestTree()
		result = tree.FindNodeByKey(0)
		self.assertTrue(result.Node is nodes['2'])
		self.assertTrue(result.NodeHasKey is False)
		self.assertTrue(result.ToLeft is True)

	def test_FindNodeByKeyNotExistingRight(self):
		(tree, nodes) = self.getTestTree()
		result = tree.FindNodeByKey(10)
		self.assertTrue(result.Node is nodes['8'])
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
		testKey = 1
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.AddKeyValue(testKey, testKey)
		findResult = tree.FindNodeByKey(testKey)
		self.assertTrue(findResult.NodeHasKey)
		self.assertTrue(nodes['2'].LeftChild is findResult.Node)

	def test_AddKeyValueToRight(self):
		(tree, nodes) = self.getTestTree()
		testKey = 10
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.AddKeyValue(testKey, testKey)
		findResult = tree.FindNodeByKey(testKey)
		self.assertTrue(findResult.NodeHasKey)
		self.assertTrue(nodes['8'].RightChild is findResult.Node)

	def test_AddKeyValueAlreadyExisting(self):
		(tree, nodes) = self.getTestTree()
		testKey = 7
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.AddKeyValue(testKey, testKey)
		self.assertFalse(tree.AddKeyValue(testKey, testKey))

	def test_FinMinMaxFromRootMin(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes['5'], False) is nodes['2'])

	def test_FinMinMaxFromRootMax(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes['5'], True) is nodes['8'])

	def test_FinMinMaxFromSubtreeMin(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes['3'], False) is nodes['2'])

	def test_FinMinMaxFromSubtreeMax(self):
		(tree, nodes) = self.getTestTree()
		self.assertTrue(tree.FinMinMax(nodes['7'], True) is nodes['8'])

	def test_DeleteNodeByKeyNotExisting(self):
		(tree, nodes) = self.getTestTree()
		self.assertFalse(tree.DeleteNodeByKey(1))

	def test_DeleteNodeByKeyEmpty(self):
		tree = BST(None)
		self.assertFalse(tree.DeleteNodeByKey(1))

	def test_DeleteNodeByKeyOneNode(self):
		testKey = 1
		node = BSTNode(testKey, testKey, None)
		tree = BST(node)
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(tree.Root is None)

	def test_DeleteNodeByKeyWithNoChild(self):
		(tree, nodes) = self.getTestTree()
		testKey = 2
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes['3'].LeftChild is None)

	def test_DeleteNodeByKeyWithOnlyLeftChild(self):
		(tree, nodes) = self.getTestTree()
		nodes['3'].RightChild = None
		testKey = 3
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes['5'].LeftChild is nodes['2'])
		self.assertTrue(nodes['2'].Parent is nodes['5'])

	def test_DeleteNodeByKeyWithOnlyRightChild(self):
		(tree, nodes) = self.getTestTree()
		nodes['3'].LeftChild = None
		testKey = 3
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(nodes['5'].LeftChild is nodes['4'])
		self.assertTrue(nodes['4'].Parent is nodes['5'])

	def test_DeleteNodeByKeyWithBothChild(self):
		(tree, nodes) = self.getTestTree()
		testKey = 5
		self.assertTrue(tree.FindNodeByKey(testKey).NodeHasKey)
		tree.DeleteNodeByKey(testKey)
		self.assertFalse(tree.FindNodeByKey(testKey).NodeHasKey)
		self.assertTrue(tree.Root is nodes['6'])
		self.assertTrue(nodes['6'].Parent is None)
		self.assertTrue(nodes['6'].LeftChild is nodes['3'])
		self.assertTrue(nodes['6'].RightChild is nodes['7'])
		self.assertTrue(nodes['3'].Parent is nodes['6'])
		self.assertTrue(nodes['7'].Parent is nodes['6'])
		self.assertTrue(nodes['7'].LeftChild is None)

	def test_CountEmpty(self):
		tree = BST(None)
		self.assertEqual(tree.Count(), 0)

	def test_CountOneNode(self):
		node = BSTNode(1, 1, None)
		tree = BST(node)
		self.assertEqual(tree.Count(), 1)

	def test_Count(self):
		(tree, nodes) = self.getTestTree()
		self.assertEqual(tree.Count(), 7)

if __name__ == '__main__':
	unittest.main()