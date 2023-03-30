class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        total = 0
        for i in range( len(nums)):
            n ^= nums[i]
            total ^= i
        
        return total ^ n