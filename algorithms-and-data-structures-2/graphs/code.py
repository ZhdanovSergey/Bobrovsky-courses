class Vertex:

	def __init__(self, val):
		self.Value = val

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
		new_index = next((index for index, vertex in enumerate(self.vertex) if vertex is None), None)

		if new_index is None:
			return False

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
		return bool(self.m_adjacency[v1][v2] or self.m_adjacency[v2][v1])
	
	def AddEdge(self, v1, v2):
		# добавление ребра между вершинами v1 и v2
		self._setAdjacencyValue(v1, v2, 1)
	
	def RemoveEdge(self, v1, v2):
		# удаление ребра между вершинами v1 и v2
		self._setAdjacencyValue(v1, v2, 0)