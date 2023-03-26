class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2

            # the number is found
            if nums[mid] == target:
                
                start, end = 0, 0
                # check the number before the mid
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                mid += 1
                start = mid

                # check the number after the mid
                while mid < len(nums) and nums[mid] == target:
                    mid += 1
                mid -= 1
                end = mid

                # return start and positions
                return [start, end]

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [-1,-1]