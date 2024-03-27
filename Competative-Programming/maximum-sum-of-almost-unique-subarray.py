class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        ans = -1
        total = sum(nums[0:k-1])
        store = Counter(nums[0:k-1])
        left = 0

        for i in range(k-1, len(nums)):
            store[ nums[i] ] += 1
            total += nums[i]

            # make sure there are m-unique elements
            if len(store) >= m:
                ans = max(ans, total)

            store[ nums[left] ] -= 1
            if store[ nums[left] ] == 0:
                store.pop( nums[left] )

            total -= nums[left]
            left += 1

        return ans if ans != -1 else 0