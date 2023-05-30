class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # edge cases
        if len(nums) <= 2:
            return max(nums)

        # Dynamic programming part
        # for each move we have two choices
        # choice - 1: 
        #   -> take previous value on memo without taking current house money
        #       dp[i]  = dp[i - 1] => there should gap so don't take current house money
        # choice - 2: 
        #   -> take 2nd-previous value on memo by taking current house money 
        #        so that there will be a gap between the previous and current houses
        #     dp[i] = dp[i - 1] + nums[i] => there is a gap so take current house money

        size = len(nums)
        memo = [0] * ( size  )
        memo[0], memo[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, size ):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])

        # at the end the maximum money will be stored
        return memo[-1]