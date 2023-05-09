class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        # this question is similar with no need to explain
        # 2208. Minimum Operations to Halve Array Sum
        # 378. Kth Smallest Element in a Sorted Matrix
        # 1962. Remove Stones to Minimize the Total
        nums = [-i for i in nums]
        heapq.heapify(nums)
        total = 0
        for _ in range(k):
            n = -heapq.heappop(nums)
            total += n

            n = ceil(n/3)
            heapq.heappush(nums, -n)

        return total