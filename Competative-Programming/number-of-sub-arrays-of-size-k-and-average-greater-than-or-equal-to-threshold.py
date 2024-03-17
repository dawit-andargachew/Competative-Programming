class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0, k - 1
        ans, total = 0, sum( arr[0:k])

        if total/k >= threshold:
            ans += 1

        right += 1
        while right < len(arr):
            total += arr[right]
            total -= arr[left]

            if total/k >= threshold:
                ans += 1
            
            left += 1
            right += 1

        return ans
        