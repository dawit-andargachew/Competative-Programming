class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i , j = 0 , 0        
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1        
        
        i += 1
        answer = i
        while i < len(nums):
            nums[i] = "_"
            i += 1
        return answer
            
        
        