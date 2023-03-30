test_case = int(input())

for _ in range(test_case):
   
    n = int(input())

    if n == 1:
        print(3)

    elif n & (n-1) == 0:
        print(n + 1)
    else:
        print(n & -n)
