class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        prod = 1
        count = left = 0
        for idx, val in enumerate(nums):
            prod *= val
            while prod >= k and left <= idx:
                prod /= nums[left]
                left += 1
            count += idx - left + 1

        return count
        