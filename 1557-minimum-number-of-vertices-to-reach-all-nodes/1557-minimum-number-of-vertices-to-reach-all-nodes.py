class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # the minimum number of vertices to make all nodes reachable is simply count nodes
        # which doesn't have incoming edges
        
        # store all vertices in list, which are from 0 to n - 1
        allEdges =[ * range(n)]
        
        # make a Vertice -1, if it has incoming edges
        for e in edges:
            allEdges[e[1]] = -1
        
        # Identify vertices which doesn't have incoming edges
        answer = [v for v in allEdges if v != -1]

        return answer