class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # merging part
        def Merge(left_p, right_p):
            temp = []
            
            i,j = 0, 0
            while i < len(left_p) and j < len(right_p):
                if left_p[i] <= right_p[j]:
                    temp.append( left_p[i] )
                    i += 1
                else:
                    temp.append( right_p[j] )
                    j += 1
            
            while i < len(left_p):
                temp.append( left_p[i])
                i += 1
            
            while j < len(right_p):
                temp.append( right_p[j])
                j += 1
            
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