import queue


class Vertex:

	def __init__(self, val):
		self.Value = val
		self.Hit = False


class SimpleGraph:
	
	def __init__(self, size):
		self.max_vertex = size
		self.m_adjacency = [[0] * size for _ in range(size)]
		self.vertex = [None] * size
		
		
	def _getVerticesCount(self):
		return self.vertex.index(None) if None in self.vertex else self.max_vertex


	def _setAdjacencyValue(self, v1, v2, value):
		self.m_adjacency[v1][v2] = value
		self.m_adjacency[v2][v1] = value
		
		
	def _resetAllHits(self):
		for index in range(self._getVerticesCount()):
			self.vertex[index].Hit = False
			
			
	def _getAdjIndexGen(self, gen_index, filter_func = lambda i: True):
		return (i for i in range(self._getVerticesCount()) if self.IsEdge(i, gen_index) and filter_func(i))


	def _getOtherAdjIndexGen(self, gen_index, filter_func = lambda i: True):
		return self._getAdjIndexGen(gen_index, lambda i: i != gen_index and filter_func(i))
		
		
	def AddVertex(self, v):
		# ваш код добавления новой вершины
		# с значением value 
		# в свободное место массива vertex
		if None not in self.vertex:
			return False

		self.vertex[self._getVerticesCount()] = Vertex(v)
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
		def DepthFirstSearchhRecursively(current_index):
			current_vertex = self.vertex[current_index]
			current_vertex.Hit = True
			stack.append(current_vertex)
			
			for index in self._getAdjIndexGen(current_index, lambda i: i == VTo):
				stack.append(self.vertex[index])
				return stack
					
			for index in self._getAdjIndexGen(current_index, lambda i: not self.vertex[i].Hit):
				path = DepthFirstSearchhRecursively(index)
				if path is not None:
					return path

			stack.pop()

		stack = []
		self._resetAllHits()
		DepthFirstSearchhRecursively(VFrom)
		return stack


	def BreadthFirstSearch(self, VFrom, VTo):
		# узлы задаются позициями в списке vertex
		# возвращается список узлов -- путь из VFrom в VTo
		# или [] если пути нету
		def search(start_index):
			search_queue = queue.Queue()
			self._resetAllHits()
			self.vertex[start_index].Hit = True
			current_index = start_index

			while True:
				for index in self._getAdjIndexGen(current_index):
					if not self.vertex[index].Hit:
						prevIndexes[index] = current_index
						
						if index == VTo:
							return True
							
						self.vertex[index].Hit = True
						search_queue.put(index)

				if search_queue.empty():
					return False

				current_index = search_queue.get()
						
			return False
			
		def getPathByPrevIndexes():
			path = []
			current_index = VTo
			
			while current_index is not None:
				path.append(self.vertex[current_index])
				current_index = prevIndexes[current_index]
				
			return path[::-1]
			
			
		prevIndexes = [None] * self.max_vertex
		isSearchSuccess = search(VFrom)
		
		if isSearchSuccess:
			return getPathByPrevIndexes()

		if VFrom == VTo and self.IsEdge(VFrom, VTo):
			return [self.vertex[VFrom]]

		return []
		
	
	def WeakVertices(self):
		# возвращает список узлов вне треугольников
		def findTriangle(first_index):
			for second_index in self._getOtherAdjIndexGen(first_index, lambda i: i not in weak_indexes):
				third_filter = lambda i: i not in weak_indexes and i != second_index and self.IsEdge(i, second_index)
				for third_index in self._getOtherAdjIndexGen(first_index, third_filter):
					strong_indexes.update([first_index, second_index, third_index])
					return True

			weak_indexes.add(first_index)

		strong_indexes = set()
		weak_indexes = set()
		without_strong_gen = (i for i in range(self._getVerticesCount()) if i not in strong_indexes)
		
		for first_index in without_strong_gen:
			findTriangle(first_index)
		
		return [self.vertex[i] for i in weak_indexes]