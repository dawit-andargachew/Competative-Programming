class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
		# initialize dp table
        dp = [[0]*(2001) for _ in range(len(nums))]
        dp[0][1000+nums[0]] += 1
        dp[0][1000-nums[0]] += 1
        
		# state transition function
        for i in range(1, len(nums)):
            for j in range(2001):
                t1 = dp[i-1][j-nums[i]] if j-nums[i] >= 0 else 0
                t2 = dp[i-1][j+nums[i]] if j+nums[i] <= 2000 else 0
                dp[i][j] = t1+t2
				
		# result
        return dp[-1][1000+target]