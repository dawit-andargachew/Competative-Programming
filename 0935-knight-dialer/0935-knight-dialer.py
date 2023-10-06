class Solution:
    def knightDialer(self, n: int) -> int:
        arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        for _ in range(n-1):
            dp = [0 for _ in range(10)]
            dp[0] = arr[5] + arr[7]
            dp[1] = arr[6] + arr[8]
            dp[2] = arr[3] + arr[7]
            dp[3] = arr[2] + arr[8] + arr[9]
            dp[4] = 0
            dp[5] = arr[0] + arr[6] + arr[9]
            dp[6] = arr[1] + arr[5]
            dp[7] = arr[0] + arr[2]
            dp[8] = arr[1] + arr[3]
            dp[9] = arr[3] + arr[5]
            arr = dp
        return sum(arr) % (10**9+7)