class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        max_val = 0
        left = -1
        n = len(nums)
        for i in range( n ):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                left = i
                break

        if left != -1:
            while left < n:
                temp = left
                while left + 1 < n and nums[left + 1] % 2 != nums[left] % 2 and nums[left + 1] <= threshold:
                    left += 1
                
                max_val = max(max_val, left - temp + 1)
                left += 1
                
                #  move elements greater than threshold
                temp = left
                for i in range(temp, n):
                    left = i
                    if nums[i] % 2 == 0 and nums[i] <= threshold:
                        break
                
        return max_val