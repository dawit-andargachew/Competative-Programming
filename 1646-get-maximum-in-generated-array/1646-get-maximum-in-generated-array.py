class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n <= 1:
            return n
            
        memo = [0] * (n + 1)
        memo[1] = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                memo[i] = memo[i//2]
            else:
                memo[i] = memo[i//2] + memo[i//2 + 1]
        
        return max(memo)