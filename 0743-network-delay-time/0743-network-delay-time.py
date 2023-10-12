class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = {}
        for time in times:
            frm, to, val = time
            if frm not in graph:
                graph[frm] = []
                
            graph[frm].append((to, val))
            
        ls = [float('inf')]*N
        
        self.search(graph, K, ls)
        
        if sum(ls) == float('inf'):
            return -1
        else:
            return max(ls)

    def search(self, graph, K, ls):
        q = [(K, 0)]
        ls[K-1] = 0
        while len(q) > 0:
            ele, dis = q.pop(0)
            if ele in graph:
                for kid in graph[ele]:
                    node, val = kid
                    if ls[node-1] > dis + val:
                        ls[node-1] = dis + val
                        q.append((node, dis+val))
        