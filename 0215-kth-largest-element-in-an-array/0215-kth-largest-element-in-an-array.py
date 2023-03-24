class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # apply quick sort and in every part check wheather the kth number
        result = -1
        def Quick(start, end):
            nonlocal result

            pivot = nums[start]
            write = start + 1

            for read in range(start + 1, end + 1):
                if pivot >= nums[read]:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1 

            nums[start], nums[write - 1] = nums[write - 1], nums[start]

            if len(nums) - ( write - 1) == k :
                result = nums[write - 1]
                return

            elif len(nums) - ( write - 1) < k:
                Quick(start, write - 2)
            else:
                Quick(write, end)

        Quick(0, len(nums) - 1)
        
        return result
    