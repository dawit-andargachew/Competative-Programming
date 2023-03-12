class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, acc = [], []
        map = defaultdict(int)
        
        for i in nums:
            map[i] += 1
            
        def backtrack():
            if len(acc) == len(nums):
                ans.append( acc[:] )
                return
                
            for n in map:
                
                if map[n] > 0:
                    map[n] -= 1
                    acc.append(n)
                    backtrack()
                    
                    acc.pop()
                    map[n] += 1
        backtrack()
        return ans