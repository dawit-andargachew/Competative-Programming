class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        # EXCEPTION - WHAT IF ALL VALUES ARE THE SAME
        if len( Counter(nums)) == 1:
            if target % nums[0] == 0: # remainder is zero, so target can be generated
                return target // nums[0]
            else:
                return -1

        # multiply arr before finding the min-window size
        base = total = sum(nums)
        count = 2 # the array should be doubled even if total > target
        while total <= target:
            total += base
            count += 1
        # increase array size by count time
        nums = nums * count

        # find minimum window size
        ans = 1_000_000_000_000
        total = left = 0

        for i in range( len(nums) ):
            total += nums[i]
            while left < i and total > target:
                total -= nums[left]
                left += 1

            if total == target:
                ans = min(ans, i - left + 1)

        return ans if ans != 1_000_000_000_000 else -1     