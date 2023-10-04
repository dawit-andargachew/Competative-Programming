class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def makeContri(start, end, path):
            path.append(start)
            visited.add(start)

            if start == end:
                for node in path:
                    contri[node] += 1
                return True
            
            for nei in adj[start]:
                if nei not in visited and makeContri(nei, end, path):
                    return True
            path.pop()
            return False
        
        contri = [0] * n

        for start, end in trips:
            visited = set()
            makeContri(start, end, [])
        
        dp = {}
        
        def dfs(node, parent, halve):
            if (node, halve) in dp:
                return dp[(node, halve)]

            res1 = float("inf")
            if not halve:
                res1 = price[node] // 2 * contri[node] 

                for nei in adj[node]:
                    if nei != parent:
                        res1 += dfs(nei, node, True)
            
            res2 = price[node] * contri[node]

            for nei in adj[node]:
                    if nei != parent:
                        res2 += dfs(nei, node, False)
            
            dp[(node, halve)] = min(res1, res2)

            return dp[(node, halve)]
        
        return dfs(0, -1, False)