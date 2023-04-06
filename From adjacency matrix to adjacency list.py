n = int(input())

for _ in range(n):
    row = list(map(int, input().split()))

    temp = []
    for i in range(len(row)):
        if row[i] == 1:
            temp.append(i + 1)
    
    print(len(temp), *temp)
