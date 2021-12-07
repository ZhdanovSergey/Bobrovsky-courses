import unittest

from code import Vertex, SimpleGraph


class HeapTests(unittest.TestCase):
    def checkVertexAdjacency(self, graph, index, arr):
        self.assertTrue(graph.m_adjacency[index] == arr)

        for i in range(graph.max_vertex):
            self.assertTrue(graph.m_adjacency[i][index] == arr[index])

    def checkEdge(self, graph, v1, v2, value):
        self.assertTrue(graph.m_adjacency[v1][v2] == value)
        self.assertTrue(graph.m_adjacency[v2][v1] == value)

    def addVertexes(self, graph, arr):
        for val in arr:
            graph.AddVertex(val)


    def test_AddVertexEmpty(self):
        graph = SimpleGraph(5)
        result = graph.AddVertex(0)
        self.assertTrue(result)
        self.assertTrue(isinstance(graph.vertex[0], Vertex))
        self.assertTrue(graph.vertex[0].Value == 0)
        self.checkVertexAdjacency(graph, 0, [0] * 5)


    def test_AddVertex(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        result = graph.AddVertex(1)
        self.assertTrue(result)
        self.assertTrue(isinstance(graph.vertex[1], Vertex))
        self.assertTrue(graph.vertex[1].Value == 1)
        self.checkVertexAdjacency(graph, 1, [0] * 5)


    def test_AddVertexFull(self):
        graph = SimpleGraph(2)
        graph.AddVertex(0)
        graph.AddVertex(1)
        result = graph.AddVertex(2)
        self.assertFalse(result)


    def test_AddEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1])
        self.checkEdge(graph, 0, 1, 0)
        graph.AddEdge(0, 1)
        self.checkEdge(graph, 0, 1, 1)


    def test_RemoveEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1])
        graph.AddEdge(0, 1)
        self.checkEdge(graph, 0, 1, 1)
        graph.RemoveEdge(1, 0)
        self.checkEdge(graph, 0, 1, 0)


    def test_RemoveVertex(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.RemoveVertex(0)
        self.checkVertexAdjacency(graph, 0, [0] * 5)

    def test_DepthFirstSearchSingleVertexWithoutEdge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        result = graph.DepthFirstSearch(0, 0)
        self.assertTrue(result == [], result)


    def test_DepthFirstSearchSingleVertexWithEdge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        graph.AddEdge(0, 0)
        result = graph.DepthFirstSearch(0, 0)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[0]], result)


    def test_DepthFirstSearchTwoVertexWithoutEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1])
        result = graph.DepthFirstSearch(0, 1)
        self.assertTrue(result == [], result)


    def test_DepthFirstSearchTwoVertexWithEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1])
        graph.AddEdge(0, 1)
        result = graph.DepthFirstSearch(0, 1)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[1]], result)


    def test_DepthFirstSearchThreeVertexWithoutEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        result = graph.DepthFirstSearch(0, 2)
        self.assertTrue(result == [], result)

    def test_DepthFirstSearchThreeVertexWithEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        result = graph.DepthFirstSearch(0, 2)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[2]], result)


    def test_DepthFirstSearchThreeVertexWithTwoEdges(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        result = graph.DepthFirstSearch(0, 2)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[1], graph.vertex[2]], result)
        
        
    def test_BreadthFirstSearchSingleVertexWithoutEdge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        result = graph.BreadthFirstSearch(0, 0)
        self.assertTrue(result == [], result)


    def test_BreadthFirstSearchSingleVertexWithEdge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        graph.AddEdge(0, 0)
        result = graph.BreadthFirstSearch(0, 0)
        self.assertTrue(result == [graph.vertex[0]], result)


    def test_BreadthFirstSearchTwoVertexWithoutEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1])
        result = graph.BreadthFirstSearch(0, 1)
        self.assertTrue(result == [], result)


    def test_BreadthFirstSearchTwoVertexWithEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1])
        graph.AddEdge(0, 1)
        result = graph.BreadthFirstSearch(0, 1)
        # print(result)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[1]], result)


    def test_BreadthFirstSearchThreeVertexWithoutEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        result = graph.BreadthFirstSearch(0, 2)
        self.assertTrue(result == [], result)

    def test_BreadthFirstSearchThreeVertexWithEdge(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        result = graph.BreadthFirstSearch(0, 2)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[2]], result)


    def test_BreadthFirstSearchThreeVertexWithTwoEdges(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        result = graph.BreadthFirstSearch(0, 2)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[1], graph.vertex[2]], result)
        
        
    def test_BreadthFirstSearchWithDifferentPaths(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2, 3, 4])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 4)
        graph.AddEdge(4, 0)
        result = graph.BreadthFirstSearch(0, 2)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[1], graph.vertex[2]], result)
        
    def test_BreadthFirstSearchWithCycle(self):
        graph = SimpleGraph(5)
        self.addVertexes(graph, [0, 1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 1)
        graph.AddEdge(1, 2)
        result = graph.BreadthFirstSearch(0, 2)
        self.assertTrue(result == [graph.vertex[0], graph.vertex[1], graph.vertex[2]], result)


if __name__ == '__main__':
    unittest.main()