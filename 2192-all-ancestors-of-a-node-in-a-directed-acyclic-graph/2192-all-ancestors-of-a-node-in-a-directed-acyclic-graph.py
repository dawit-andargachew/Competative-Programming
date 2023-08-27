class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]

        g = defaultdict(list)

        for u, v in edges:
            g[v].append(u)
        
        def dfs(node, curr):
            for v in g[curr]:
                if v not in ans[node]:
                    dfs(node, v)
                    ans[node].append(v)  
        
        for i in range(n):
            dfs(i,i)

        for k in ans:
            k.sort()
            
        return ans 