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

	def _FindNodeByKeyRecursive(self, key, current_node):
		if key < current_node.NodeKey and current_node.LeftChild is not None:
			return self._FindNodeByKeyRecursive(self, key, current_node.LeftChild)
		elif key > current_node.NodeKey and current_node.RightChild is not None:
			return self._FindNodeByKeyRecursive(self, key, current_node.RightChild)

		result = BSTFind()
		result.Node = current_node

		if key == current_node.NodeKey:
			result.NodeHasKey = True
		elif key < current_node.NodeKey:
			result.ToLeft = True

		return result

	def FindNodeByKey(self, key):
		# ищем в дереве узел и сопутствующую информацию по ключу
		# возвращает BSTFind
		if self.Root is None:
			return BSTFind()

		return self._FindNodeByKeyRecursive(key, self.Root)

	def AddKeyValue(self, key, val):
		# добавляем ключ-значение в дерево
		find_result = self.FindNodeByKey(key)

		if find_result.NodeHasKey:
			return False

		finded_node = find_result.Node

		if find_result.ToLeft:
			node.LeftChild = BSTNode(key, val, node)
		else:
			node.RightChild = BSTNode(key, val, node)
  
	def FinMinMax(self, FromNode, FindMax):
		# ищем максимальный/минимальный ключ в поддереве
		# возвращается объект типа BSTNode
		if (FindMax and FromNode.RightChild is None)\
			or (not FindMax and FromNode.LeftChild is None):
			return FromNode
		elif FindMax:
			return self.FinMinMax(FromNode.RightChild, FindMax)
		else:
			return self.FinMinMax(FromNode.LeftChild, FindMax)

	
	def DeleteNodeByKey(self, key):
		# удаляем узел по ключу
		find_result = self.FindNodeByKey(key)
		if not find_result.NodeHasKey:
			return False

		node = find_result.Node
		parent = node.Parent
		isLeftChild = node.NodeKey < parent.NodeKey

		# if node.LeftChild is None\
		# 	and node.RightChild is None:
			

	def Count(self):
		return 0 # количество узлов в дереве