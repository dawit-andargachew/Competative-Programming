class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            count = hasApple[node]
            time = 0
            for child in graph[node]:
                if child != parent:
                    cnt, t = dfs(child, node)
                    if cnt > 0:
                        time += t + 2
                        count += cnt
                
            return count, time
        
        res = dfs(0, -1)
        return res[1]