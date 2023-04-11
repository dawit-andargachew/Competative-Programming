class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        # similar with 785. Is Graph Bipartite?

        graph = defaultdict(list)
        for d in dislikes:
            graph[ d[0] ].append( d[1] )
            graph[ d[1] ].append( d[0] )

        def dfs(node):
            for i in graph[node]:
                if i in color:
                    if color[i] == color[node]:
                        return False
                else:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
            return True
        
        color = {}
        for g in graph:
            if g not in color:
                color[g] = 0
                if not dfs(g):
                    return False

        return True