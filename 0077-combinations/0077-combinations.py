class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        # we have two branches at each level so 
        # time complexiy = 2^n + for copying
        # see the other implementation
        ans = []        
        def backtrack(idx, acc):
            
            if len(acc) == k:
                ans.append(acc[:])
                return
            
            if idx > n:
                return
        
            acc.append(idx)
            backtrack( idx + 1, acc)
            acc.pop()
            backtrack( idx + 1, acc)
            
        backtrack(1, [])        
        
        
        return ans