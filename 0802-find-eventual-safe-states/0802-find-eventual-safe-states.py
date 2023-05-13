class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # It can be done DFS. But what is a safe node.
        # Safe node is a node with out a cycle is called a safe node
        # So the task is simply to extract nodes which are not part of a cycle

        grid, color = defaultdict(list), [0] * len(graph)

        for i in range ( len(graph) ):
            grid[i] = []
            for node in graph[i]:
                grid[i].append(node)
        
        order = []
        def topSort(node):
            if color[node] == 1:
                return False
            
            color[node] = 1
            for n in grid[node]:
                if color[n] == 2:
                    continue
                if not topSort(n):
                    return False
            
            color[node] = 2
            order.append(node)
            return True
        # 0 -> not visited 1-> part of the current visit  2-> already visited and is safe node
        # make a bfs on every node, which are not visited and
        for key in range( len(graph) ):
            if color[key] != 2:
                topSort(key)
            
        order.sort()
        return order