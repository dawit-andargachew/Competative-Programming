test = int(input())

for t in range(test):

    a = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    isYes = True
    for i in range(1, len(nums)):

        if nums[i] - nums[i - 1] > 1:
            isYes = False
            break
    
    if isYes:
        print("YES")
    else:
        print("NO")
