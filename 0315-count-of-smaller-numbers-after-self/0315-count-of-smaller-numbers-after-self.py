class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # hold the answer to be returned and updated in the merging process
        result = [0] * len(nums) 

        # what if the array contain duplicate values? like [5,2,6,1,5,1]
        # so we need to consider their respective indices as well when we sort
        # Modify the original array and replace each value with [val, index] pair
        for i in range( len(nums) ): 
            nums[i] = [nums[i], i]

        # this function merge each list by there value and count smallers as well
        # to store the count of each number, it must access the indices found on [val, indices]
        def merge_and_count(left, right):
            
            # count the number smaller than it self to the left and updated the "result" array
            count, i , j = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    count += 1
                    j += 1
                else:
                    result[ left[i][1] ] += count
                    i += 1

            # if the left part is not iterated to the end, fill the rest with value of count
            while i < len(left):
                result[ left[i][1] ] += count
                i += 1
            merge = left + right
            merge.sort(key=lambda x:x[0])
            
            return merge
        
        # dividing process
        def split_half(l, r):
            if l == r:
                return [nums[r]]
                
            mid = (l + r)//2
            left = split_half(l, mid)
            right = split_half( mid + 1, r)

            return merge_and_count(left, right)
        
        split_half(0, len(nums) - 1)

        return result