class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        # to count the number of letters in a sub-tree, we need to do
        # 1, prevent traversing through the parent node
        # 2, keep track of labes frequency in the subtree
        # 3, update the number of labels in the sub-tree

        graph = defaultdict(list)
        for a, b in edges:
            graph[ a ].append( b )        
            graph[ b ].append( a )

        answer = [0]*n
        # each child-node will return a dict to its parent-node
        # so parent node can get the label with their corresponding frequencies
        def Tree_DFS(index, parent):
            
            count = Counter()
            for edge in graph[index]:

                # 1, it is a tree, so block the bath through its parent 
                if edge != parent:
                    #2, keep labels frequency in the entire sub-tree
                    count += Tree_DFS(edge, index)
            
            # 3, update the number of labels in the sub-tree
            count[ labels[index] ] += 1
            answer[index] = count[ labels[index] ]

            return count
        
        #Start DFS from root, and take -1 as dfs 
        Tree_DFS(0,-1)
        
        return answer