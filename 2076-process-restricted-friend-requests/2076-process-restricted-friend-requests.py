class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def friendRequests(self, n, restr, requests):
        dsu, ans = DSU(n), []
        for x, y in requests:
            x_p, y_p = dsu.find(x), dsu.find(y)
            other = True
            for a, b in restr:
                a_p, b_p = dsu.find(a), dsu.find(b)
                if set([a_p, b_p]) == set([x_p, y_p]):
                    other = False
                    break
                    
            ans += [other]
            if other:
                dsu.union(x, y)
                
        return ans