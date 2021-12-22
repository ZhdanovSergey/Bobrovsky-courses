import math

class BSTNode:
	def __init__(self, key, parent):
		self.NodeKey = key # ключ узла
		self.Parent = parent # родитель или None для корня
		self.LeftChild = None # левый потомок
		self.RightChild = None # правый потомок
		self.Level = 0 if parent is None else parent.Level + 1 # уровень узла
		
class BalancedBST:
	def __init__(self):
		self.Root = None # корень дерева

	def GenerateTree(self, arr):
	# создаём дерево с нуля из неотсортированного массива a
		def generateTreeRecursively(parent_node, start_index, end_index):
			middle_index = math.ceil((start_index + end_index) / 2)
			current_node = BSTNode(arr[middle_index], parent_node)

			if end_index - start_index > 0:
				current_node.LeftChild = generateTreeRecursively(current_node, start_index, middle_index - 1)

			if end_index - start_index > 1:
				current_node.RightChild = generateTreeRecursively(current_node, middle_index + 1, end_index)
			
			return current_node

		if len(arr) > 0:
			arr.sort()
			self.Root = generateTreeRecursively(None, 0, len(arr) - 1)

		return self

	def IsBalanced(self, root_node):

		def checkIsSubtreeBalanced(node):
			(is_left_balanced, left_max_level) = checkIsSubtreeBalanced(node.LeftChild) if node.LeftChild is not None else (True, node.Level)
			(is_right_balanced, right_max_level) = checkIsSubtreeBalanced(node.RightChild) if node.RightChild is not None else (True, node.Level)
			is_current_balanced = is_left_balanced and is_right_balanced and abs(left_max_level - right_max_level) <= 1
			return (is_current_balanced, max(left_max_level, right_max_level))

		is_tree_balanced = True
		if root_node is not None:
			(is_tree_balanced, _) = checkIsSubtreeBalanced(root_node)
		return is_tree_balanced # сбалансировано ли дерево с корнем root_node