class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
# solution link 
# - https://leetcode.com/problems/k-th-symbol-in-grammar/solutions/945679/python-recursive-everything-you-need-to-know/
        if N == 1: 
            return 0

        half = 2**(N - 2)
        
        if K > half:
            if self.kthGrammar(N - 1, K - half) == 0:
                return 1
            else:
                return 0
        else:
            return self.kthGrammar(N - 1, K)