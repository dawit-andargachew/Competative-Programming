class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            
            # if i + 1 == nums[ nums[i] - 1], there is a duplicate number
            if (i + 1) != nums[ nums[i] - 1]:
                if nums[i] == nums[ nums[i] - 1]:
                    return nums[i]
                
                nums[ nums[i] - 1], nums[i] = nums[i], nums[ nums[i] - 1]
                
            else:
                i += 1