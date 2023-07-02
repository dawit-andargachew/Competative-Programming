class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        def dfs(node):

            if node == destination:
                return True
        
            visited.add(node)
            for n in graph[node]:
                if n == destination:
                    return True

                if n not in visited:
                    if dfs(n):
                        return True
            
        return dfs(source)
        