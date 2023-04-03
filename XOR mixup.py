for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    i, j = 0, 0
    while i < len(nums):

        temp = 0
        while j < len(nums):
            if i != j:
                temp ^= nums[j]
            j += 1

        if temp == nums[i]:
            print(temp)
            i = len(nums)
        i += 1
