# from collections import deque
class Solution:
    def __init__(self):
        self.slots = {  0:[9,1], 1:[0,2], 2:[1,3], 3:[2,4], 4:[3,5], 
                        5:[4,6], 6:[5,7], 7:[6,8], 8:[7,9], 9:[8,0]   }
        
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        trap = set(deadends)
        if start in deadends: return -1
        queue = deque([[start, 0]])
        used = set()
        used.add(start)
        
        while queue:
            curr, moves = queue.popleft()
            if curr == target: 
                return moves
            for i in range(4):
                for slot in self.slots[int(curr[i])]:
                    move = curr[:i] + str(slot) + curr[i+1:]
                    if move not in trap and move not in used:
                        queue.append([move, moves + 1])
                        used.add(move)


        return -1