from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        sorted_list = SortedList(nums[0:k])
        ans = [0] * (len(nums) - k + 1)
        ans[0] = sorted_list[x-1] if sorted_list[x-1] < 0  else 0

        for i in range(k, len(nums)):
            sorted_list.discard(nums[i-k])
            sorted_list.add(nums[i])
            ans[i - k + 1] = sorted_list[x-1] if sorted_list[x-1] < 0  else 0

        return ans