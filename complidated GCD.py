
def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)

a, b = map(int, input().split())

if a == 1 or b - a >= 1:
    print(1)
elif b - a == 0:
    print(a)
# else:
#     complicatedGCD = a
#     for i in range(a + 1, b + 1):
#         complicatedGCD = GCD(complicatedGCD, i)

#     print(complicatedGCD)
