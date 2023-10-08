class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        # we want to move half to city A and half to B

        total = 0
        for i in range( len(costs)):
            costs[i].append( costs[i][0] - costs[i][1] )
        
        # sort the array by their cost 
        costs.sort( key=lambda x:x[2])

        num = len(costs)//2        
        # the first half got to A
        for i in range(num):
            total += costs[i][0]
        
        num *=2
        # then take half to city B
        for i in range(num//2, num):
            total +=costs[i][1]

        return total