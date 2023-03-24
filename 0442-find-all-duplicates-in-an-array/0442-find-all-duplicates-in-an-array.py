class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        # sort with cyclic sort
        while i < len(nums):
            
            if (i + 1) != nums[i] and nums[ nums[i] - 1] != nums[i]:
                idx = nums[i]
                nums[ nums[i] - 1], nums[i] = idx, nums[ idx - 1]
            
            else:
                i += 1

        temp = []
        # element which are out of orderd are duplicates
        for i in range( len(nums)):
            if (i + 1 )!= nums[i]:
                temp.append( nums[i])

        return temp