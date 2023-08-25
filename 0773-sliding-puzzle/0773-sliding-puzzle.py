class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        neighbor = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        q = []
        start_list = []
        for row in board:
            for num in row:
                start_list.append(str(num))
        start = "".join(start_list)
        q.append(start)

        visited = set()
        step = 0

        while len(q) > 0:
            length = len(q)
            for i in range(length):
                status = q.pop(0)
                if status == target:
                    return step
                index = status.find("0")
                for next_pos in neighbor[index]:
                    num = status[next_pos]
                    status_list = list(status)
                    status_list[next_pos] = "0"
                    status_list[index] = num
                    next_status = "".join(status_list)
                    if next_status not in visited:
                        visited.add(next_status)
                        q.append(next_status)
            step += 1
            
        return -1
