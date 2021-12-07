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


    def _setAdjacencyValue(self, v1, v2, value):
        self.m_adjacency[v1][v2] = value
        self.m_adjacency[v2][v1] = value
        
    def _resetAllHits(self):
        for vertex in self.vertex:
            if vertex is None:
                break
            vertex.Hit = False
            
    def _getAdjacentIndexesGenerator(self, gen_index):
        return (index for index in range(self.max_vertex) if self.IsEdge(gen_index, index))
        
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
        def DepthFirstSearchhRecursively(current_index):
            current_vertex = self.vertex[current_index]
            current_vertex.Hit = True
            stack.append(current_vertex)
            
            for index in self._getAdjacentIndexesGenerator(current_index):
                if index == VTo:
                    stack.append(self.vertex[index])
                    return stack
                    
            for index in self._getAdjacentIndexesGenerator(current_index):
                if not self.vertex[index].Hit:
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
        def BreadthFirstSearchRecursively(current_index):            
            for index in self._getAdjacentIndexesGenerator(current_index):
                if not self.vertex[index].Hit:
                    prevIndexes[index] = current_index
                    self.vertex[index].Hit = True
                    
                    if index == VTo:
                        return True
                        
                    search_queue.put(index)
                    
            if search_queue.empty():
                return False
                
            return BreadthFirstSearchRecursively(search_queue.get())
            
        def GetPathByPrevIndexes():
            if VFrom == VTo:
                return [self.vertex[VFrom]]
            
            path = []
            current_index = VTo
            
            while current_index is not None:
                path.append(self.vertex[current_index])
                current_index = prevIndexes[current_index]
                
            return path[::-1]
            
            
        search_queue = queue.Queue()
        prevIndexes = [None] * self.max_vertex
        self._resetAllHits()
        self.vertex[VFrom].Hit = True
        
        if BreadthFirstSearchRecursively(VFrom):
            return GetPathByPrevIndexes()
            
        return []