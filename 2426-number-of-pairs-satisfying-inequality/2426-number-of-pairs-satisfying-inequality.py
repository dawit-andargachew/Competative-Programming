class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        pairs = 0
        def merge_and_count(left, right):
            nonlocal pairs

            i , j, curr_pairs = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= (right[j] + diff):
                    curr_pairs += (len(right) - j)
                    i += 1
                else:
                    j += 1

            # add to the global variable
            pairs += curr_pairs

            merge = left + right
            merge.sort()
            return merge

        def split_half(l, r):
            if l == r:
                return [ new_nums[l] ]
            
            mid = ( l + r)//2
            left = split_half(l, mid)
            right = split_half( mid + 1, r)

            return merge_and_count(left, right)

        # create new array by merge those
        # to find the number of pairs satisfying the inequality the equation should be rearranged 
        #      nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        #      nums1[i] -  nums2[i] =  nums1[j] -  nums2[j] + diff => rearranged equation
        #     - rearranging the equation helps only to focus on one array instead of two 
        #  now find i where nums[i] <= nums[i] + diff
        new_nums = []
        for i in range( len(nums1) ):
            new_nums.append( nums1[i] - nums2[i])
        
        split_half(0, len(new_nums) - 1)
        
        return pairs