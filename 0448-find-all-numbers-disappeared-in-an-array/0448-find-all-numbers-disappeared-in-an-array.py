class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # lets apply cyclic  sort and to handle repeated numbers ignore them if they are already placed on their correct possitions
        i = 0
        while i < len(nums):

            if nums[i] != (i + 1) and nums[nums[i] - 1] != nums[i]:
                idx = nums[i]
                nums[i] = nums[ nums[i] - 1]
                nums[ idx - 1] = idx
            else:
                i += 1

        missed = []
        for i in range(len(nums)):
            if (i + 1) != nums[i]:
                missed.append(i + 1)

        return missed