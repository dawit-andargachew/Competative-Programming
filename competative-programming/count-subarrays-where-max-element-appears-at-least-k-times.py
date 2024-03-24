class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_val, n = max( nums ), len( nums )
        count = left = ans = right = 0
        
        while right < n:
            if nums[right] == max_val:
                count += 1
            
            while count == k and left <= right: # left < n, works as well
                ans += n - right
                if nums[left] == max_val:
                    count -= 1
                left += 1
            right += 1
        
        return ans

        