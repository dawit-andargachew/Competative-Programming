n = int(input())

NumberOfOnes = 0
for _ in range(n):
    row = list(map(int, input().split()))

    for r in row:
        if r == 1:
            NumberOfOnes +=1 
    
print(NumberOfOnes//2)
