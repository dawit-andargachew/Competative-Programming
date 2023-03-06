class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # to maximize the number of childers sort both `g` and `s`.
        # then compare each values of `g` and `s`
        g.sort()
        s.sort()

        child_number, i, j = 0, 0, 0
        
        while i < len(g) and j < len(s):
            if g[ i ] <= s[ j ]:
                child_number += 1
                i += 1
                j += 1
            else:
                j += 1

        return child_number