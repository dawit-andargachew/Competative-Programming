class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        g, s, res = [0] * n, [0] * n, 0
        
        # For each soldier, we search the next greater and smaller
        for i in range(n - 1):
            for j in range(i + 1, n):
                if rating[j] > rating[i]: 
                    g[i] += 1
                else:
                    s[i] += 1
        
        for i in range(n - 2):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    res += g[j]
                else:
                    res += s[j]
        
        return res