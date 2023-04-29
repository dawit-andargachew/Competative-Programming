class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:

        # make binary search on answer and BFS
        R, C = len(grid), len(grid[0])
        fire = [[float('inf')] * C for _ in range(R)]
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fire[r][c] = 0
                    q.appendleft((r, c))
        

        step = 0
        while q:
            nq = deque()
            while q:
                r, c = q.pop() 
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == 0 and fire[rr][cc] == float('inf'):
                        nq.appendleft((rr, cc))
                        fire[rr][cc] = min(fire[rr][cc], step + 1)
            step += 1
            q = nq

        def check(mid):
            q = deque([(0, 0)])
            v = {(0, 0): mid} 
            while q:
                r, c = q.pop()
                step = v[r, c] 
                if r == R - 1 and c == C - 1:
                    return True
                for dr, dc in  [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    rr, cc = dr + r, c + dc
                    if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == 0 and (rr, cc) not in v and (step + 1 < fire[rr][cc] or (rr, cc) == (R - 1, C - 1) and step + 1 <= fire[rr][cc] ):
                        q.appendleft((rr, cc))
                        v[rr, cc] = step + 1
            return False

        lo, hi = 0, 1000000000
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        if check(lo):
            return lo 
        return -1