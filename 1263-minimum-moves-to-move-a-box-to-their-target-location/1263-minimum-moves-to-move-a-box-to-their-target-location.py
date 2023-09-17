class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        neighbors = ((-1,0), (1,0), (0,-1), (0,1)) 
        
        # initial values
        for i, j in product(range(m), range(n)):
            if   grid[i][j] == "B": box    = i, j
            elif grid[i][j] == "S": player = i, j
            elif grid[i][j] == "T": target = i, j
        
        # helper function
        def not_wall(i, j):
            return  0 <= i < m and 0 <= j < n and grid[i][j] !="#"
            
        def connected(s, d):
            queue = [s]
            seen = set(queue)
            for i, j in queue:
                for di, dj in neighbors:
                    ii, jj = i + di, j + dj
                    if not_wall(ii, jj) and (ii, jj) != box and (ii, jj) not in seen: 
                        queue.append((ii, jj))
                        seen.add((ii, jj))
                if d in seen: return True
            return False 
        
        final = set()
        for di, dj in neighbors:
            final.add( (target, (target[0]+di, target[1]+dj)) )
        
        moves = 0 
        #initial position
        queue = [(box, player)]
        seen = set(queue)
        
        # make a bfs by level 
        while queue: 
            temp = []
            for box, player in queue:
                i, j = box
                for di, dj in neighbors:
                    if not_wall(i+di, j+dj) and ((i+di, j+dj), (i, j)) not in seen and not_wall(i-di, j-dj) and connected(player, (i-di, j-dj)):
                        temp.append(((i+di, j+dj), (i, j)))
                        seen.add(((i+di, j+dj), (i, j)))
            queue = temp
            moves += 1
            if seen & final:
                # final position is when => arrive at target
                return moves
        return -1 