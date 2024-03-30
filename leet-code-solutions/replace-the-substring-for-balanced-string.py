class Solution:
    def balancedString(self, s: str) -> int:
        
        extra = defaultdict(int)
        for i in ['Q','W','E','R']:
            dif = s.count(i) - len(s)//4
            extra[i] = dif if dif > 0 else 0

        # no need to replace
        if extra["Q"] == extra["W"] == extra["R"] == extra["E"] == len(s)//4:
            return 0
        
        temp, ans, left = defaultdict(int), len(s), 0

        for i in range( len(s) ):
            
            temp[ s[i] ] += 1

           # remove the left part the curr letter has more than extra
            while left < len(s) and temp[ s[left] ] > extra[ s[left] ]:
                temp[ s[left] ] -= 1
                left += 1

            # to be replaced, it should have at least the size of extra
            # then update answer to get the minimum windows size
            if temp["Q"] >= extra["Q"] and temp["W"] >= extra["W"] and \
                temp["E"] >= extra["E"] and temp["R"] >= extra["R"]:
                ans = min(ans, i - left + 1)
        
        return ans
