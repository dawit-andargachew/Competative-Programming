class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, visited):
            if visited[node]:
                return 0

            visited[node] = True
            return 1 + sum(dfs(neighbor, visited) for neighbor in graph[node])

        # build adjacency graph
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # calculate sizes of connected components
        visited = [False] * n
        sizes = []
        for i in range(n):
            sizes.append(dfs(i, visited))

        total = 0
        for i in range(n):
            total += sizes[i] * (n - sizes[i] )
        
        return total//2