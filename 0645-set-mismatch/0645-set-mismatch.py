class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        i = 0
        # sort them with cylic sort [ by taking in to account duplicate values]
        while i < len(nums):

            if nums[i] != (i + 1) and nums[nums[i] - 1] != nums[i]:
                idx = nums[i]
                nums[i] = nums[ idx - 1]
                nums[ idx - 1] = idx
            else:
                i += 1

        mismatch = []
        # find the mismatch number
        for i in range(len(nums)):
            
            if (i + 1) != nums[i]:
                mismatch.append( nums[i] )
                mismatch.append( i + 1)
    
        return mismatch