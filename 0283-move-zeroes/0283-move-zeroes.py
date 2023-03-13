class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        left, right = 0, 0
        
        # get the first non-zero position
        # while nums[left] == 0:
        #     left += 1
        
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
                
            right += 1
        
        # replace with zero after moving non-zero numbers
        while left < len(nums):
            nums[left] = 0
            left += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        