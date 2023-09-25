class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        s=set()
        s.add(stones[0])
        s.add(-stones[0])
        
        dp=set()
        for i in range(1,len(stones)):
            for j in s:
                dp.add(abs(j-stones[i]))
                dp.add(abs(j+stones[i]))
            s=dp
            dp=set()
            
        return min(s)