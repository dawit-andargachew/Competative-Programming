class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for val in range(target, num - 1, -1):
                dp[val] = dp[val] or dp[val - num]
        return dp[-1]
