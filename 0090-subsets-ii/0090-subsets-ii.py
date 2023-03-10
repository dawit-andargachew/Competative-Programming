class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        acc = []
        nums.sort()

        def backtrack(idx):
            if acc not in ans:
                ans.append(acc[:])

            if idx > len(nums):
                return

            for i in range(idx, len(nums)):
                acc.append(nums[i])
                backtrack(i + 1)
                acc.pop()

        backtrack(0)
        
        return ans
        