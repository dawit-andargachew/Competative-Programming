class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        m = sum(x for x in nums if x > 0)
        heap = [(-m, 0)] 
        vals = sorted(abs(x) for x in nums)
        for _ in range(k): 
            x, i = heappop(heap) 
            if i < len(vals): 
                heappush(heap, (x+vals[i], i+1))
                if i:
                    heappush(heap, (x-vals[i-1]+vals[i], i+1))
        return -x