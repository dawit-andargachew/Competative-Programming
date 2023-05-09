class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        # heapify => is min heap so make piles negative
        # loop k times and do the opration on the largest value
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            num = -heapq.heappop(piles)
            num -= num//2
            heapq.heappush(piles, -num)

        # make values positive
        return -sum(piles)