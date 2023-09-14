class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meeting_counts = [0] * n
        meeting_ends_heap = []
        free_rooms_heap = list(range(n))
        heapq.heapify(free_rooms_heap)

        meetings.sort()

        for start, end in meetings:
            while meeting_ends_heap and start >= meeting_ends_heap[0][0]:
                temp, room_id = heapq.heappop(meeting_ends_heap)
                heapq.heappush(free_rooms_heap, room_id)
            
            delay = 0
            if free_rooms_heap:
                room_id = heapq.heappop(free_rooms_heap)
            else:
                delay = meeting_ends_heap[0][0] - start
                temp, room_id = heapq.heappop(meeting_ends_heap)

            heapq.heappush(meeting_ends_heap, [end + delay, room_id])
            meeting_counts[room_id] += 1
        
        return meeting_counts.index(max(meeting_counts))