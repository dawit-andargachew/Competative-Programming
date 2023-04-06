n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


source, sink = [], []
for i in range(n):

    isSource, isSink = False, False

    row = graph[i]
    if 1 in row:
        isSource = True

    for j in range(n):
        if graph[j][i] == 1:
            isSink = True
            break

    # add to sink and source lists
    if not isSource and not isSink:
        sink.append(i +1)
        source.append(i + 1)
    elif not isSource and isSink:
        sink.append(i + 1)
    elif isSource and not isSink:
        source.append(i + 1)


print(len(source), *source)
print(len(sink), *sink)

