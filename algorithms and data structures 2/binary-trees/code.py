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
			return self._FindNodeByKeyRecursive(key, currentNode.LeftChild)
		elif key > currentNode.NodeKey and currentNode.RightChild is not None:
			return self._FindNodeByKeyRecursive(key, currentNode.RightChild)

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

		if findedNode is None:
			self.Root = newNode
		elif findResult.ToLeft:
			findedNode.LeftChild = newNode
		else:
			findedNode.RightChild = newNode

		return True
	
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

	def _DeleteNodeWithMaxOneChild(self, node):
		parent = node.Parent
		successor = None

		if node.RightChild is not None:
			successor = node.RightChild
		elif node.LeftChild is not None:
			successor = node.LeftChild

		if parent is None:
			self.Root = successor
		elif node.NodeKey < parent.NodeKey:
			parent.LeftChild = successor
		else:
			parent.RightChild = successor

		if successor is not None:
			successor.Parent = parent

	def DeleteNodeByKey(self, key):
		# удаляем узел по ключу
		findResult = self.FindNodeByKey(key)

		if not findResult.NodeHasKey:
			return False

		node = findResult.Node

		if node.LeftChild is None or node.RightChild is None:
			self._DeleteNodeWithMaxOneChild(node)
			return True

		parent = findResult.Node.Parent
		successor = self.FinMinMax(node.RightChild, False)
		self._DeleteNodeWithMaxOneChild(successor)
		successor.LeftChild = node.LeftChild
		successor.RightChild = node.RightChild
		node.LeftChild.Parent = successor

		if node.RightChild is not None:
			node.RightChild.Parent = successor

		successor.Parent = parent

		if parent is None:
			self.Root = successor
		elif successor.NodeKey < parent.NodeKey:
			parent.LeftChild = successor
		else:
			parent.RightChild = successor

		return True

	def _CountNodes(self, currentNode):
		self._counter += 1

		if currentNode.LeftChild is not None:
			self._CountNodes(currentNode.LeftChild)

		if currentNode.RightChild is not None:
			self._CountNodes(currentNode.RightChild)

	def Count(self):
		self._counter = 0

		if self.Root is not None:
			self._CountNodes(self.Root)
		
		return self._counter