class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0]*(target+1)
        dp[0] = 0
        
        for num in nums:
            if num<=target:
                dp[num] += 1

        for i in range(1, len(dp)):
            for j in nums:
                if i>j:
                    dp[i]+=dp[i-j]
        return dp[target]