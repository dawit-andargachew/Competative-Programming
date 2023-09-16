class Solution:
    def eatenApples(self, A: List[int], D: List[int]) -> int:
        
        ans, idx, N = 0, 0, len(A)
        height = []
        while idx < N or height:
            if idx < N and A[idx] > 0:
                heappush(height, [idx + D[idx], A[idx]])
            while height and (height[0][0] <= idx or height[0][1] <= 0):
                heappop(height)
            if height:
                height[0][1] -= 1
                ans += 1
            idx += 1
            
        return ans 