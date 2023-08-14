class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums):
            # dynamic programming - decide each problem by its sub-problems:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])

            return dp[-1]
        
        # edge cases:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # either use first house and can't use last or last and not first:
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))