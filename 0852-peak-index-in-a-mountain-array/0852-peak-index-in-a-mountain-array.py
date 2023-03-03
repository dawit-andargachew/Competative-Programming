class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        right = len( arr) - 1

        while left <= right:
            mid = left + (right - left)//2

            if max(arr[mid], arr[mid-1], arr[mid+1]) == arr[mid]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid  - 1
        # return -1
