import unittest
from code import SimpleTreeNode, SimpleTree


class EvenTreesTests(unittest.TestCase):
	def CreateTree(self):
		nodes = [SimpleTreeNode(i, None) for i in range(11)]
		tree = SimpleTree(nodes[1])
		tree.AddChild(nodes[1], nodes[2])
		tree.AddChild(nodes[2], nodes[5])
		tree.AddChild(nodes[2], nodes[7])
		tree.AddChild(nodes[1], nodes[3])
		tree.AddChild(nodes[3], nodes[4])
		tree.AddChild(nodes[1], nodes[6])
		tree.AddChild(nodes[6], nodes[8])
		tree.AddChild(nodes[8], nodes[9])
		tree.AddChild(nodes[8], nodes[10])

		return (tree, nodes)

	def test_EvenTree(self):
		(tree, nodes) = self.CreateTree()
		result = tree.EvenTrees()
		self.assertTrue(result == [nodes[1], nodes[3], nodes[1], nodes[6]], result)


	def test_Count(self):
		(tree, nodes) = self.CreateTree()
		result = tree.Count()
		self.assertTrue(result == 10, result)

	def test_GetAllNodes(self):
		(tree, nodes) = self.CreateTree()
		result = tree.GetAllNodes()
		self.assertTrue(True, result)

if __name__ == '__main__':
	unittest.main()