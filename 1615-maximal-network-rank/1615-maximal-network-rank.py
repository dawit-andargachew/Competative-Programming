class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for r in roads:
            graph[ r[1] ].add( r[0] )
            graph[ r[0] ].add( r[1] )

        rank = 0
        # check every combination of nodes
        for i in graph:
            for j in graph:
                if i == j: # i and j points to the same node, so skip
                    continue
                
                current = len(graph[i]) + len(graph[j])

                # if they are connected with each other, take one path not two
                if i in graph[j]:
                    current -= 1 # remove redundant path from the total
                    
                rank = max(rank, current)

        return rank