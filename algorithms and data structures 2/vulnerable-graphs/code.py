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
            
            
    def _getAdjIndexGen(self, gen_index, cond_func = lambda i: True):
        return (i for i in range(self._getVerticesCount()) if self.IsEdge(gen_index, i) and cond_func(i))
        
        
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
            VTo_match_adj_gen = (i for i in self._getAdjIndexGen(current_index, lambda i: i == VTo))
            not_hit_adj_gen = (i for i in self._getAdjIndexGen(current_index, lambda i: not self.vertex[i].Hit))
            
            for index in VTo_match_adj_gen:
                stack.append(self.vertex[index])
                return stack
                    
            for index in not_hit_adj_gen:
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
        
    
    # def WeakVertices(self):
        # # возвращает список узлов вне треугольников
        # strong_indexes = set()
        # weak_indexes = set()
        
        # for first_index in range(self._getVerticesCount())
            # if first_index not in strong_indexes:
                # for second_index in self._getAdjacentIndexesGenerator(first_index):
                    # if second_index not in weak_indexes\
                        # and second_index != first_index:
                        # for third_index in range(self._getVerticesCount()):
                            # if third_index not in weak_indexes\
                                # and third_index != second_index\
                                # and third_index != first_index:
                                
        
        # return []