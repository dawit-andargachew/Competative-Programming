from collections import defaultdict

n = int(input())
k = int(input())
graph = defaultdict(list)

for _ in range(k):
    temp = list(map(int, input().split()))

    if temp[0] == 1:

        graph[temp[1]].append(temp[2])
        graph[temp[2]].append(temp[1])
    else:

        if len(graph[temp[1]]) > 0:
            print(*graph[temp[1]])
