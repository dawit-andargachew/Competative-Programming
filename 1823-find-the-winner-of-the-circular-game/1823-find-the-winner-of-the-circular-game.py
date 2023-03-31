class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        # put the first k - 1 elements at the end of the queue until we have one element
        d = deque()
        for i in range(1, n + 1):
            d.append(i)
        
        while len(d) > 1:

            moves = 0 # updated latter
            if k <= len(d):
                moves = k
            else:
                if k % len(d) != 0:
                    moves = k % len(d)
                else:
                    moves = len(d)

            while moves > 1:
                d.append( d.popleft() )
                moves -= 1
            
            d.popleft()        

        return d[0]
        