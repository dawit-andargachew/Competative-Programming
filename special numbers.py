t = int(input())

# the kth special number is simply
# idenify the indicies of on bits and sum up all the powers of n
# take n = 4 and k = 5
# k = 101, one bit indices are[ 0, 2]
# so answer is 4 ** 0 + 4 ** 2
for _ in range(t):
    n, k = map(int, input().split())
    indices, i = [], 0
    
    while k > 0:
        if  k & 1 == 1:
            indices.append(i)

        i += 1
        k >>= 1

    ans = 0
    for i in indices:
        ans += (n**i)
    mod = 10**9 + 7
    print(ans %  mod)
