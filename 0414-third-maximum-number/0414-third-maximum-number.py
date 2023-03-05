class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # to get the third maximu, sort the array and remove dupliate elements
        # then return nums[ len(nums) - 3] => which is the third maximum number

        nums = [*set(nums)] # remove duplicates
        nums.sort()
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[1]
        else:
            return nums[ len(nums) - 3 ]
        