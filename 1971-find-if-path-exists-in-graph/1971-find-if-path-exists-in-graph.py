class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Lets use Union Find even if it can be implemented by DFS easily

        # initialize the dict to store representative for each node
        represent = {i: i for i in range(n) }

        def union(u, v):
            u_rep = find(u)
            v_rep = find(v)
            represent[ v_rep ] = u_rep
        
        def find(x):
            while x != represent[x]:
                x = represent[x]
            return x

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)