class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        minimums = [nums[0]]
        for i in range(1, len(nums)):
            minimums.append(minimums[i - 1] & nums[i])
            
        abs_min = minimums[-1]
        
        if abs_min > 0:
            return 1
        
        res = 1
        cur = nums[-1]
        i = len(nums) - 1
        while i > 0:
            if cur == abs_min and minimums[i - 1] == abs_min:
                res += 1
                cur = nums[i - 1]
            else:
                cur &= nums[i - 1]
            i -= 1
        return res
        