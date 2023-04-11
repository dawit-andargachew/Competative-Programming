class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # similar with 886. Possible Bipartition
        def dfs(i):
            for nb in graph[i]:
                if nb in color:
                    if color[nb] == color[i]:
                        return False
                else: 
                    color[nb] = 1 - color[i]
                    if not dfs(nb):
                        return False
            return True

        color = {}
        for i in range(len(graph)):
            if i not in color: 
                color[i] = 0 
                if not dfs(i):
                    return False

        return True