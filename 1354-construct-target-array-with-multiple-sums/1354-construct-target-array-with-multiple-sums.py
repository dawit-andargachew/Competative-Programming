class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        h = [-x for x in target]
        heapify(h)
        while h[0] < -1:
            v = -heappop(h)
            if total - v == 1:
                return True
            if total - v == 0:
                return False
            u = v % (total - v)
            if u == 0 or u == v:
                return False
            heappush(h, -u)
            total = total - v + u
        return True    