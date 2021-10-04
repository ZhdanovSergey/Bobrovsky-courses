class BSTNode:
	
	def __init__(self, key, val, parent):
		self.NodeKey = key # ключ узла
		self.NodeValue = val # значение в узле
		self.Parent = parent # родитель или None для корня
		self.LeftChild = None # левый потомок
		self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

	def __init__(self):
		self.Node = None # None если 
		# в дереве вообще нету узлов

		self.NodeHasKey = False # True если узел найден
		self.ToLeft = False # True, если родительскому узлу надо 
		# добавить новый узел левым потомком

class BST:

	def __init__(self, node):
		self.Root = node # корень дерева, или None

	def WideAllNodes(self):
		def collectNodes(level_arr):
			result_arr.extend(level_arr)
			next_level_arr = []

			for node in level_arr:
				if (node.LeftChild is not None):
					next_level_arr.append(node.LeftChild)

				if (node.RightChild is not None):
					next_level_arr.append(node.RightChild)

			if (len(next_level_arr)):
				collectNodes(next_level_arr)

		result_arr = []
		if (self.Root is not None):
			collectNodes([self.Root])

		return tuple(result_arr)

	def DeepAllNodes(self, order):
		def collectNodes(node, order):
			if (order == 2):
				result_arr.append(node)

			if (node.LeftChild is not None):
				collectNodes(node.LeftChild, order)

			if (order == 0):
				result_arr.append(node)

			if (node.RightChild is not None):
				collectNodes(node.RightChild, order)

			if (order == 1):
				result_arr.append(node)

		result_arr = []

		if (self.Root is not None):
			collectNodes(self.Root, order)

		return tuple(result_arr)