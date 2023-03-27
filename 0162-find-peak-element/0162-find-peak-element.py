class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # adding negative elemnts to the end will guarantee the end elements will be peak values
        # and help us to prevent index out of range 
        nums.append(float('-inf'))
        nums.insert(0, float('-inf'))

        l, h = 0 , len(nums) - 1
        while l <= h:
            mid = (l + h)//2

            # this condition checks the value is peak or not
            if max( nums[mid], nums[mid - 1], nums[mid + 1]) == nums[mid]:
                return mid - 1 # each indices is shift by one since one element is added
            
            # in each step, the search space will reduce by one depending on their monotonicity
            # in here it is increasing so the left part of mid is expected to have peak value
            elif nums[mid] > nums[mid + 1] :
                h = mid - 1
            else:
                l = mid + 1
                
            # # Here is also the above case with different if condition. 
            # # this one check the whether to move to the right of mid
            
            # elif nums[mid] > nums[mid - 1] :
            #     l = mid + 1
            # else:
            #     h = mid - 1