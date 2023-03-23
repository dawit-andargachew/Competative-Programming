class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # the numbers are from 0 to n, and the goal is to find the missing number
        # add all numbers from 0 to n return the difference between it and sum of nums
        # simply sum( from 0 to n) - sum(nums) gives the missing number
        # Time: O(N) and space: O(1)
        total = 0
        for i in range ( len(nums) + 1):
            total += i

        nums_sum = sum(nums)

        return total - nums_sum