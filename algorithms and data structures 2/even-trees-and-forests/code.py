class SimpleTreeNode:
	def __init__(self, val, parent):
		self.NodeValue = val # значение в узле
		self.Parent = parent # родитель или None для корня
		self.Children = [] # список дочерних узлов
		self.subtreeNodesCounter = 1

	
class SimpleTree:
	def __init__(self, root):
		self.Root = root # корень, может быть None


	def _UpdateSubtreeNodesCounters(self, node, value):
		node.subtreeNodesCounter += value
		if node.Parent is not None:
			self._UpdateSubtreeNodesCounters(node.Parent, value)


	def _CollectFilteredNodes(self, filter_function):
		def collectFilteredNodesRecursively(current_node, filter_function):
			if filter_function(current_node):
				collected_nodes.append(current_node)
			for node in current_node.Children:
				collectFilteredNodesRecursively(node, filter_function)

		collected_nodes = []
		collectFilteredNodesRecursively(self.Root, filter_function)
		return collected_nodes


	def _CountFilteredNodes(self, filter_function):
		def countFilteredNodesRecursively(current_node, filter_function):
			if filter_function(current_node):
				nonlocal counter
				counter += 1
			for node in current_node.Children:
				countFilteredNodesRecursively(node, filter_function)

		counter = 0
		countFilteredNodesRecursively(self.Root, filter_function)
		return counter

	
	def AddChild(self, ParentNode, NewChild):
		# ваш код добавления нового дочернего узла существующему ParentNode
		NewChild.Parent = ParentNode
		ParentNode.Children.append(NewChild)
		self._UpdateSubtreeNodesCounters(ParentNode, NewChild.subtreeNodesCounter)

  
	def DeleteNode(self, NodeToDelete):
		# ваш код удаления существующего узла NodeToDelete
		NodeToDelete.Parent.Children.remove(NodeToDelete)
		self._UpdateSubtreeNodesCounters(NodeToDelete.Parent, -NodeToDelete.subtreeNodesCounter)


	def GetAllNodes(self):
		# ваш код выдачи всех узлов дерева в определённом порядке
		return self._CollectFilteredNodes(lambda x: True)


	def FindNodesByValue(self, val):
		# ваш код поиска узлов по значению
		return self._CollectFilteredNodes(lambda x: x.NodeValue == val)

   
	def MoveNode(self, OriginalNode, NewParent):
		# ваш код перемещения узла вместе с его поддеревом -- 
		# в качестве дочернего для узла NewParent
		self.DeleteNode(OriginalNode)
		self.AddChild(NewParent, OriginalNode)

   
	def Count(self):
		# количество всех узлов в дереве
		return self._CountFilteredNodes(lambda x: True)


	def LeafCount(self):
		# количество листьев в дереве
		return self._CountFilteredNodes(lambda x: len(x.Children) == 0)


	def EvenTrees(self):
		def fillNodesToSplitRecursively(node):
			for child in node.Children:
				if child.subtreeNodesCounter % 2 == 0:
					nodes_to_split.extend([node, child])

				fillNodesToSplitRecursively(child)

		nodes_to_split = []
		fillNodesToSplitRecursively(self.Root)

		return nodes_to_split