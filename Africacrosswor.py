n, m = map(int, input().split())
grid  = []

for _ in range(n):
    temp =list( input())
    grid.append(temp)

crossed = set()
for row in range(n):
    for col in range(m):
        curr = grid[row][col]

        for c in range(m):
            
            if grid[row][c] == curr and c != col:
                crossed.add((row, c))
        
        for r in range(n):
            if grid[r][col] == curr and r != row:
               crossed.add((r,col))


for r, c in crossed:
    grid[r][c] = 0

for r in range(n):
    for c in range(m):
        if grid[r][c] != 0:
            print(grid[r][c], end="")
