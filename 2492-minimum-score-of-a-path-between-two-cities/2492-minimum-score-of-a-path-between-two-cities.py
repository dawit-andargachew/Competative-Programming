class DisJointSet:
    def __init__(self):
        self.representative = {}

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        self.representative[y_rep] = x_rep

    def find(self, x):
        if x not in self.representative:
            self.representative[x] = x
            return x

        val = x
        while x != self.representative[x]:
            x = self.representative[x]
        
        # path compression
        while x != self.representative[val]:
            parent = self.representative[val]
            self.representative[val] = x
            val = parent
            
        return x

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

       # lets use Union Find technique. 
       # but how do we now the current node leads to n?
       # if find(n) == find(node) => they are on the same group

       # group the nodes
        obj = DisJointSet()
        for x, y, _ in roads:
            obj.union(x, y)
        
        # find the minimum edge by checking the representative for each node
        min_distance = float('inf')
        for x, y, distance in roads:
            if obj.find(x) == obj.find(n):
                min_distance = min( min_distance, distance)

        return min_distance