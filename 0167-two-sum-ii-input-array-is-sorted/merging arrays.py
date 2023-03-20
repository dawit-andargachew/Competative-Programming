n, m = map(int, input().split())
nums = list(map(int, input().split()))
arr = list(map(int, input().split()))
 
i, j = 0, 0
counter = 0
 
while j < len(arr):
 
    while i < len(nums) and nums[i] < arr[j]:
        i += 1
        counter += 1
    
    print(counter, end=" ")
    j += 1
