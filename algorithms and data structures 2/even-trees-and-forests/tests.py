import unittest
from code import SimpleTreeNode, SimpleTree


class EvenTreesTests(unittest.TestCase):
	def test_EvenTree(self):
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

		result = tree.EvenTrees()
		self.assertTrue(result == [nodes[1], nodes[3], nodes[1], nodes[6]], result)

if __name__ == '__main__':
	unittest.main()