class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left, right = 0, 0

        while right < len(nums):
            
            # move unique elements to the front of the array
            nums[left] = nums[right]
            left += 1

            # if concecutive elements are identical, move the pointer forward
            while right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right += 1
            right += 1

        return left