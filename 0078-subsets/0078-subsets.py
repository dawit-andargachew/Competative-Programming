class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        acc = []
        
        def backtrack(idx):
            
            if len(acc) <= idx:
                ans.append(acc[:])
                
            if idx > len(nums):
                return
            
            for i in range( idx, len(nums) ):
                
                if nums[i] not in acc:
                    acc.append( nums[i] )
                    backtrack(i + 1)
                    acc.pop()
        
        
        backtrack(0)
        return ans