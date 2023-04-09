class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # remove n, where n <= 0
        arr = [n for n in nums if n > 0]
        arr.sort()

        if not arr:
            return 1
            
        if arr[0] != 1:
            return 1
        
        # if there is a gap greater than 1 there is missing number
        for i in range( len(arr) - 1):
            if arr[i + 1] - arr[i] > 1:
                return arr[i] + 1
        # else the missing number is not in the given list
        return arr[-1] + 1