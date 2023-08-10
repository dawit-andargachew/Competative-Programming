class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        high, low, answer = 0, 0, float('inf')
        while high < len(nums):
            if high - low + 1 == k:
                answer = min(answer, nums[high] - nums[low])
                low += 1
            high += 1
        
        return answer
        