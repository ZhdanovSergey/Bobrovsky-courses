class Vertex:

	def __init__(self, val):
		self.Value = val
		self.Hit = False


class SimpleGraph:
	
	def __init__(self, size):
		self.max_vertex = size
		self.m_adjacency = [[0] * size for _ in range(size)]
		self.vertex = [None] * size


	def _setAdjacencyValue(self, v1, v2, value):
		self.m_adjacency[v1][v2] = value
		self.m_adjacency[v2][v1] = value

		
	def AddVertex(self, v):
		# ваш код добавления новой вершины
		# с значением value 
		# в свободное место массива vertex
		if None not in self.vertex:
			return False

		new_index = self.vertex.index(None)
		self.vertex[new_index] = Vertex(v)
		return True


	# здесь и далее, параметры v -- индекс вершины
	# в списке  vertex
	def RemoveVertex(self, v):
		# ваш код удаления вершины со всеми её рёбрами
		self.vertex[v] = None

		for i in range(self.max_vertex):
			self._setAdjacencyValue(v, i, 0)

	
	def IsEdge(self, v1, v2):
		# True если есть ребро между вершинами v1 и v2
		return self.m_adjacency[v1][v2] == 1

	
	def AddEdge(self, v1, v2):
		# добавление ребра между вершинами v1 и v2
		self._setAdjacencyValue(v1, v2, 1)

	
	def RemoveEdge(self, v1, v2):
		# удаление ребра между вершинами v1 и v2
		self._setAdjacencyValue(v1, v2, 0)


	def DepthFirstSearch(self, VFrom, VTo):
		# узлы задаются позициями в списке vertex
		# возвращается список узлов -- путь из VFrom в VTo
		# или [] если пути нету
		def findPathRecursively(current_index):
			current_vertex = self.vertex[current_index]
			current_vertex.Hit = True
			stack.append(current_vertex)

			for index in range(self.max_vertex):
				if self.IsEdge(current_index, index) and index == VTo:
					stack.append(self.vertex[index])
					return stack

			for index in range(self.max_vertex):
				if self.IsEdge(current_index, index) and not self.vertex[index].Hit:
					path = findPathRecursively(index)
					if path is not None:
						return path

			stack.pop()


		for vertex in self.vertex:
			if vertex is None:
				break
			vertex.Hit = False

		stack = []
		findPathRecursively(VFrom)
		return stack