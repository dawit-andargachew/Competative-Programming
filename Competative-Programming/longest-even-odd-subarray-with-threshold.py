class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        max_val = 0
        left = -1
        n = len(nums)
        for i in range( n ):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                left = i
                break

        it_end  = False
        if left != -1:
            # print("loop begins and here is the value, ", left)
            while left < n:
                # if it_end:
                #     left = n + 1

                temp = left
                while left + 1 < n and nums[left + 1] % 2 != nums[left] % 2 and nums[left + 1] <= threshold:
                    left += 1
                
                # print("temp ", temp)
                # print("left ", left)
                # print()
                max_val = max(max_val, left - temp + 1)
                left += 1
                
                #  move elements greater than threshold
                temp = left
                for i in range(temp, n):
                    left = i
                    # if i == n - 1:
                    #     it_end = True

                    if nums[i] % 2 == 0 and nums[i] <= threshold:
                        break
                

                # if left < n and (temp == left and nums[left]%2 != 0):
                #     # print("yea broken")
                #     break
                # if temp == left:
                #     left += 1
                # if left >= n:
                #     it_end = True

        return max_val