class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []   
        acc = []
       
        # backtrack is simply two things
        # 1, check valid cases
        # 2, remove the previos one and check again
        def backtrack(idx):
            
            # 1 check valid cases
            if len(acc) == len(nums):
                ans.append( acc[:] )
                return
            
            if idx > len(nums):
                return
            
            # iterate all over possible cases
            for i in range( len(nums)):
                
                # only append if it is not duplicate
                if nums[i] not in acc:
                    acc.append( nums[i] )
                    backtrack(i + 1)
                    acc.pop()
        
        backtrack(0)
        
        return ans