class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # merging part
        def Merge(left_p, right_p):
            temp = left_p + right_p
            temp.sort()
            return temp
            
        # deviding part
        def mergeSort(left, right):
            if left == right:
                return [ nums[left] ]
            
            mid = (left + right)//2
            
            left_part = mergeSort(left, mid)
            right_part = mergeSort(mid + 1, right)
            
            return Merge(left_part, right_part)
        
        return mergeSort(0, len(nums) - 1)