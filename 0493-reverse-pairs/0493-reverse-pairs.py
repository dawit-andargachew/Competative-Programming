class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        pairs = 0
        # it counts reverse pairs and return sorted list
        # sorting the list makes easy to count reverse pairs
        def Combine(left, right):
            nonlocal pairs
            
            # since the sub-array are sorted, it makes easy to find reverse pairs
            i, j = 0, 0
            while i < len(left) and j < len(right):

                if left[i] > 2 * right[j]:
                    pairs += len(left) - i
                    j += 1
                else:
                    i += 1
            
            # CUSTOM SOTRING CODE, LEFT AND RIGHT ARE SOTRED so it is like merging two sorted lists
            # sort left and right before returnig to higher level callers
            # merged, i , j = [], 0 , 0
            # while i < len(left) and j < len(right):
            #     if left[i] <= right[j]:
            #         merged.append( left[i])
            #         i += 1
            #     else:
            #         merged.append( right[j] )
            #         j += 1

            # # for left part
            # while i <len(left):
            #     merged.append( left[i] )
            #     i += 1
            
            # # for right part
            # while j < len(right):
            #     merged.append( right[j] )
            #     j += 1           
            merged = left + right
            merged.sort() 
            return merged


        # split each sub-array in to two until one element remains
        def split_into_Half(l,r):
            if l == r:
                return [nums[l]]
            
            mid = ( l + r)//2

            left = split_into_Half (l, mid)
            right = split_into_Half (mid + 1, r)
            return Combine(left,right)
        
        split_into_Half(0, len(nums) - 1)
        return pairs
