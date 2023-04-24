class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # It can be more optimized by Union Fold techinique
        # this implementation is somehow bruteforce on DFS 
        
        graph = defaultdict(list)
        for edge in edges:
            graph[ edge[0] ].append( edge[1] ) 
            graph[ edge[1] ].append( edge[0] )

        def hasCycle(node, visited, parent):

            visited.add(node)
            for i in graph[node]:
                
                # ignore ecxluded edges here
                if node in excludeEdge and i in excludeEdge:
                    continue
                
                # if i visited and i != parent, then there is a cycle in graph
                # because the graph is undirected so edge [1,2]  => 1----2 is cyclic, so to avoid this condition
                # i != parent handles that the above issue
                if i != parent and i in visited:
                    return True

                if i not in visited:
                    if hasCycle(i, visited, node):
                        return True

        def checkForCycle():
            for key in list(graph.keys()):
                if hasCycle(key, set(), key):
                    return True
            return False

        excludeEdge  = []
        for i in range( len(edges) ):
            pair = edges[ len(edges) - 1 - i] # start removing edges from the end
            excludeEdge = pair
            
            # after changing exluded edges check for cylce again,
            # if there is no cycle, return current pair
            if not checkForCycle():
                return pair