class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        # the other implementation is
        # we have n branches and each have k iterations each
        # time complexiy = n^k + for copying
        # in here, insteading of checking yes or no for every possible move, iterate over a for loop and call them

        ans = []        
        def backtrack(idx, acc):
            
            if len(acc) == k:
                ans.append(acc[:])
                return
            
            if idx > n:
                return
            
            for i in range(idx, n + 1):
                acc.append(i)
                backtrack( i + 1, acc)
                acc.pop()
            # backtrack( idx + 1, acc)
            
        backtrack(1, [])        
        
        
        return ans