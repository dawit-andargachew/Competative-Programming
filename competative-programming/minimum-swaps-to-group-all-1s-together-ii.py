class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        # the triky part is to determine the number of swaps
        # So, how?
        """
        First, by appending nums to nums, you can ignore the effect of split case.
        Then, you look at the window whose width is width. Here, width = the number of 1's in the original nums.
        This is because you have to gather all 1's in this window at the end of some swap operations.
        Therefore, the number of swap operation is the number of 0's in this window.
        The final answer should be the minimum value of this. 
        """
        
        one = nums.count(1)
        if one == 0:
            return 0

        nums = nums * 2
        
        count, ans = 0, len( nums )
        left, right = 0, 0
        while right < len( nums ):
            if nums[right] == 0:
                count += 1
            
            if right - left == one - 1:
                ans = min(ans, count)

                if nums[left] == 0:
                    count -= 1
                left += 1
            right += 1

        return ans    