class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        table = defaultdict(int)
        
        answer = -1
        for i in nums:
            table[i] += 1
            
            if table[-i] > 0:
                answer = max(answer, abs(i))
        
        return answer