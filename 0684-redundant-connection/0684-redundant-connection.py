# # MORE OPTIMIZED SOLUTION
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
#         # initialize the dictionary and rank
#         graph = {i : i for i in range(1, len(edges) + 1)}
#         rank = {i : 1 for i in range(1, len(edges) + 1)}
        
#         # optimized union, by using rank
#         def union(x, y):
#             x_val = find(x)
#             y_val = find(y)

#             if x_val == y_val:
#                 return True
#             else:
#                 # lets use the rank to make find more efficient
#                 if rank[ x_val ] > rank[ y_val ]:
#                     graph[ y_val ] = x_val
#                     rank[ x_val ] += rank[ y_val ]
#                 else:
#                     graph[ x_val ] = y_val
#                     rank[ y_val ] += rank[ x_val ]
#                 return False

#         # Optimized find, 
#         # after getting find connect each element on the path to their reference, so the depth becomes 1
#         def find(x):
#             val = x
#             while x != graph[x]:
#                 x = graph[x]
            
#             while val != graph[val]:
#                 parent = graph[val]
#                 graph[val] = x
#                 val = parent

#             return x

#         for edge in edges:
#             if union(edge[0], edge[1]):
#                 return edge

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # initialize the dictionary and rank
        graph = {i : i for i in range(1, len(edges) + 1)}
        def find(x):
            while x != graph[x]:
                x = graph[x]
            return x

        def union(x, y):
            x_val = find(x)
            y_val = find(y)

            if x_val == y_val:
                return True
            graph[ y_val ] = x_val
            return False

        for edge in edges:
            if union(edge[0], edge[1]):
                return edge