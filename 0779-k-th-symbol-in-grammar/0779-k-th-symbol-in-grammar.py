class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
# solution link 
# - https://leetcode.com/problems/k-th-symbol-in-grammar/solutions/945679/python-recursive-everything-you-need-to-know/
        if N == 1: 
            return 0
        
        # mid element is this
        half = 2**(N - 1)//2
        
        if K > half:
            return 1 - self.kthGrammar(N - 1, K - half)
        else:
            return self.kthGrammar(N - 1, K)