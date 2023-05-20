class DisJointSet:
    def __init__(self):
        self.representative = {}

    def union(self, row, col):
        row_rep = self.find( ('r', row) )
        col_rep = self.find( ('c', col) ) 

        # put ('r', val ) as a representative
        self.representative[ col_rep ] = row_rep
        self.representative[ (row, col) ] = row_rep

    def find(self, item):
        if item not in self.representative:
            self.representative[item] = item
            return item

        val = item
        while item != self.representative[item]:
            item = self.representative[item]
        
        # path compression
        while val != self.representative[val]:
            parent = self.representative[val]
            self.representative[val] = item
            val = parent

        return item

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # The goal is to remove stones in ones group. Every stone in one group except its representative can be removed
        #    And we can use Union Find, but what we need to use something for representative
        #    we can use these tuple as a key in the dictionary
        #      ('r', val ) => row and its value, 
        #      ('c', va )  => col and its value
        #      (row, col) => row and col together, 
        # Example, take [0, 1] row = 0 and col = 1
        #      ('r', val) => ('r', 0)
        #      ('c', val) => ('c', 1)
        #      (row, col) => (0, 1) 

        #  From these lets use ('r', 0) as a representative
        # At each group there will be one element afer removing the rest
        # So, the largest possible number of stones that can be removed is
        #       total number of stones - number of groups,

        dis = DisJointSet()
        for row, col in stones:
            dis.union(row, col)

        groups = set()
        for row, col in stones:
            a = dis.find( (row, col) )
            groups.add(a)

        return len(stones) - len(groups)