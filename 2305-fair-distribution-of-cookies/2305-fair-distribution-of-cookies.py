class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        bucket = [0]*k
        cookies.sort(reverse = True)
        
        minUnfair = float('inf')
        
        def backtrack(i):
            nonlocal minUnfair
            
            if i >= len(cookies):
                minUnfair = min( minUnfair, max(bucket))
                return
            
            if max(bucket) >= minUnfair:# pruning case and > or >= have no difference
                return
            
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i+1)
                bucket[j] -= cookies[i]
                
        backtrack(0)
        
        return minUnfair
            