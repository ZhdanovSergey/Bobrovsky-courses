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

	def _FindNodeByKeyRecursive(self, key, currentNode):
		if key < currentNode.NodeKey and currentNode.LeftChild is not None:
			return self._FindNodeByKeyRecursive(self, key, currentNode.LeftChild)
		elif key > currentNode.NodeKey and currentNode.RightChild is not None:
			return self._FindNodeByKeyRecursive(self, key, currentNode.RightChild)

		result = BSTFind()
		result.Node = currentNode

		if key == currentNode.NodeKey:
			result.NodeHasKey = True
		elif key < currentNode.NodeKey:
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
		findResult = self.FindNodeByKey(key)

		if findResult.NodeHasKey:
			return False

		findedNode = findResult.Node
		newNode = BSTNode(key, val, findedNode)

		if findResult.ToLeft:
			findedNode.LeftChild = newNode
		else:
			findedNode.RightChild = newNode
	
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
		findResult = self.FindNodeByKey(key)
		if not findResult.NodeHasKey:
			return False

		node = findResult.Node
		parent = node.Parent
		successor = None

		if node.LeftChild is None and node.RightChild is not None:
			successor = node.RightChild

		elif node.LeftChild is not None and node.RightChild is None:
			successor = node.LeftChild

		elif node.LeftChild is not None and node.RightChild is not None:
			successor = self.FinMinMax(node.RightChild, False)
			successor.LeftChild = node.LeftChild
			successor.RightChild = node.RightChild

		if successor is not None:
			successor.Parent = parent

		if parent is None:
			self.Root = successor
		elif node.NodeKey < parent.NodeKey:
			parent.LeftChild = successor
		else:
			parent.RightChild = successor

	def _CountNodes(self, currentNode):
		self._counter += 1

		if currentNode.LeftChild is not None:
			self._CountNodes(currentNode.LeftChild)

		if currentNode.RightChild is not None:
			self._CountNodes(currentNode.RightChild)

	def Count(self):
		self._counter = 0
		self._CountNodes(self.Root)
		
		return self._counter