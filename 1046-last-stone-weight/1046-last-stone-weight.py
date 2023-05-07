class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # lets user heapq library
        # but heapq is min-heap so to get the max element we need to make the given array negative
        
        stones = [-i for i in stones] # make the array negative
        heapq.heapify(stones) # heapify it
        
        while len(stones) > 1:
            one, two = heapq.heappop(stones), heapq.heappop(stones)
            if one != two:
                heapq.heappush(stones, (one - two))
        
        # all stones are not destroyed each other, so there is one element left
        if stones:
            # all stones are positive and must be positive when returned
            if stones[0] < 0:
                return -stones[0]
            else:
                return stones[0]
        
        # stones are destroyed each other and no stone left
        return 0