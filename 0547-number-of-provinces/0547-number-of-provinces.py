class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # The question is find the number of components in Undirected graph
        # So create the adjaceny list and make dfs on it
        
        # create adjacency list 
        graph = defaultdict(list)
        for i in range( len(isConnected)):
            for j in range( len(isConnected[0])):
                if isConnected [i][j] == 1:
                    graph[i + 1].append(j + 1)

        # make dfs on each node and keep track of visited nodes
        visited = set()
        def dfs(node):
            visited.add(node)
            for value in graph[node]:
                if value not in visited:
                    dfs(value)

        # check wheather every node is reachable or not
        provinces = 0
        for key in graph:
            if key not in visited:
                dfs(key)
                provinces += 1
        
        return provinces