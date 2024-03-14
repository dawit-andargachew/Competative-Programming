class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        ans = 0
        start, end = -1, -1
        for i in range( len(nums) ):

            # if the value is greater, make the starting point as the largest indice
            if nums[i] > right:
                start = end = i
            
            if nums[i] >= left:
                end = i
            
            # add every move, collect the number of sub-arrays we can make
            ans += end - start            

        return ans

        # for i in range(len(nums)):
        #     curr = -1
        #     for j in range(i, len(nums) ):
        #         curr = max(curr, nums[j])
        #         if left <= curr <= right:
                    # counter += 1
