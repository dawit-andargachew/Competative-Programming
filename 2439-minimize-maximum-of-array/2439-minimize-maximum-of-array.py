class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        total_sum = nums[0] 
        for i in range(1, len(nums)):
            total_sum+=nums[i]
            ans = max(ans, math.ceil(total_sum/(i+1)))
        return ans