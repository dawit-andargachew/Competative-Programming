t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    i = 0
    while i < n:
        j = i
        while j + 1 < n and a[j + 1] * a[j] > 0:
            j += 1
        ans.append(max(a[i:j + 1]))
        i = j + 1
    print(sum(ans))
