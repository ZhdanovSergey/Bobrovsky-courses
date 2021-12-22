class SimpleTreeNode:
	
	def __init__(self, val, parent):
		self.NodeValue = val # значение в узле
		self.Parent = parent # родитель или None для корня
		self.Children = [] # список дочерних узлов
	
class SimpleTree:

	def __init__(self, root):
		self.Root = root # корень, может быть None

	def _CollectFilteredNodes(self, current_node, filter_function):
		if filter_function(current_node):
			self._collected_nodes.append(current_node)
		for node in current_node.Children:
			self._CollectFilteredNodes(node, filter_function)

	def _CountFilteredNodes(self, current_node, filter_function):
		if filter_function(current_node):
			self._counter += 1
		for node in current_node.Children:
			self._CountFilteredNodes(node, filter_function)
	
	def AddChild(self, ParentNode, NewChild):
		# ваш код добавления нового дочернего узла существующему ParentNode
		NewChild.Parent = ParentNode
		ParentNode.Children.append(NewChild)
  
	def DeleteNode(self, NodeToDelete):
		# ваш код удаления существующего узла NodeToDelete
		NodeToDelete.Parent.Children.remove(NodeToDelete)

	def GetAllNodes(self):
		# ваш код выдачи всех узлов дерева в определённом порядке
		self._collected_nodes = []
		self._CollectFilteredNodes(self.Root, lambda x: True)
		return self._collected_nodes

	def FindNodesByValue(self, val):
		# ваш код поиска узлов по значению
		self._collected_nodes = []
		self._CollectFilteredNodes(self.Root, lambda x: x.NodeValue == val)
		return self._collected_nodes
   
	def MoveNode(self, OriginalNode, NewParent):
		# ваш код перемещения узла вместе с его поддеревом -- 
		# в качестве дочернего для узла NewParent
		self.DeleteNode(OriginalNode)
		self.AddChild(NewParent, OriginalNode)

   
	def Count(self):
		# количество всех узлов в дереве
		self._counter = 0
		self._CountFilteredNodes(self.Root, lambda x: True)
		return self._counter

	def LeafCount(self):
		# количество листьев в дереве
		self._counter = 0
		self._CountFilteredNodes(self.Root, lambda x: len(x.Children) == 0)
		return self._counter