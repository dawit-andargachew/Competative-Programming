class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        
        memo = [0]*(n + 1)
        memo[1], memo[2] = 1, 1
        
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        
        return memo[-1]