class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return
            
            if rank[x] >= rank[y]:
                parent[y] = x
                rank[x] += rank[y]
            else:
                parent[x] = y
                rank[y] += rank[x]
        
        def find(x):
            while x != parent[x]:
                parent[x] = x = parent[parent[x]]
            return x
        
        for i in range(n):
            union(row[2 * i] // 2, row[2*i + 1] // 2)
        
        return sum(rank[i] - 1 for i in range(n) if i == parent[i])