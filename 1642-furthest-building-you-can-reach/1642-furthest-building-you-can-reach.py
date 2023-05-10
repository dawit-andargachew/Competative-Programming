class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap, i = [], 0
        while i < len(heights):
            if i == len(heights) - 1:
                return i

            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if diff <= bricks:
                    bricks -= diff
                    heapq.heappush(heap, -diff)
                elif ladders:
                    if heap:
                        if -heap[0] > diff:
                            bricks += (-heapq.heappop(heap)) - diff
                            heapq.heappush(heap, -diff)                        
                    ladders -= 1
                else:                    
                    break            
            i += 1

        return i