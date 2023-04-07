class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        # convert the edge list to adjacency list to make it easier for dfs
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = set()
        
        # dfs function 
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    found =dfs(i)
                    if found:
                        return True
        
        
        return dfs(source)
        