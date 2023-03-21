class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # perform array operation
        for i in range( len(nums) - 1 ):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            
        # shift all non-zero numbers to the left
        left, right = 0, 0
        while right < len( nums ):

            if nums[ right ] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1  
        
        # make numbers after left pointer zero,[ after shift non-zero numbers make the rest zero]
        while left < len(nums):
            nums[left] = 0
            left += 1
        
        return nums