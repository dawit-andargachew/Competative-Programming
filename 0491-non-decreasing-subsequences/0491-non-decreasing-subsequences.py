class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans, acc = [], []
        
        # this question is similar to Combination Sum II
        def backtrack(idx):
            
            if len(acc) > 1:
                ans.append( acc[:] )
            
            visited = set() # store visited numbers
            for i in range(idx, len(nums)):

                if nums[i] in visited:
                   continue
                   
                if not acc or acc[-1] <= nums[i]:
                    acc.append( nums[i] )
                    visited.add( nums[i] )
                    backtrack( i + 1)
                    acc.pop()
        
        backtrack(0)

        return ans
