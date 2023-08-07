class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if( k == 0):
            return
        
        
        # reverse whole array
        i, j = 0, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        
        
        # reverse starting from rotating position
        pos = k % len(nums)
        
        # reverse from 0 to pos
        i, j = 0, pos - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # reverse from pos + 1 to end
        i,j = pos, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        
            
        