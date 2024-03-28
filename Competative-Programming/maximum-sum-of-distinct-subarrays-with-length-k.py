class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        ans = left = total = 0
        s = defaultdict(int)
        
        for i in range(len(nums)):
            s[ nums[i] ] += 1
            total += nums[i]

            while s[ nums[i] ] > 1 or len(s) > k:
                s[ nums[left] ] -= 1
                total -= nums[left]
                
                if s[ nums[left] ] == 0:
                    s.pop( nums[left] )
                left +=1

            if len(s) == k:
                ans = max(ans, total)
            

        return ans
        