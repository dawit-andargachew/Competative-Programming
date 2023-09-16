class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ns = len(servers)
        nt = len(tasks)
        
        free = []
        for i in range(ns):
            heapq.heappush(free, (servers[i], i, 0))
            
        busy, result = [], []
        for j in range(nt):
            while len(busy)> 0 and busy[0][0] <= j:
                time, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index, time))
                
            if len(free) > 0:
                weight, index, time = heapq.heappop(free)
            else:
                time, weight, index = heapq.heappop(busy)
            result.append(index)
            time = max(time, j) 
            heapq.heappush(busy, (time + tasks[j], weight, index))
            
        return result