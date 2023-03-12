class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        acc = []

        def backtrack(idx):
            
            # valid candidates
            if len(acc) <= len(nums):
                ans.append(acc[:])
            
            if idx > len(nums):
                return

            # generate possible candidates
            for i in range(idx, len(nums) ):
                acc.append( nums[i] )
                backtrack(i + 1)
                acc.pop()

        backtrack(0)
        return ans