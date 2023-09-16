class Solution:
    def eatenApples(self, A: List[int], D: List[int]) -> int:
        ans, idx, N = 0, 0, len(A)
        h = []
        while idx < N or h:
            if idx < N and A[idx] > 0:
                heappush(h, [idx + D[idx], A[idx]])
            while h and (h[0][0] <= idx or h[0][1] <= 0):
                heappop(h)
            if h:
                h[0][1] -= 1
                ans += 1
            idx += 1
            
        return ans 