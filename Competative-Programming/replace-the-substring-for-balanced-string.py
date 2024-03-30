class Solution:
    def balancedString(self, s: str) -> int:
        
        table = defaultdict(int)
        for i in ['Q','W','E','R']:
            extra = s.count(i) - len(s)//4
            table[i] = extra if extra > 0 else 0

        # no need to replace
        if table["Q"] == table["W"] == table["R"] == table["E"] == len(s)//4:
            return 0
        
        temp, ans, left, i = defaultdict(int), len(s), 0, 0

        # while i < len(s) and (temp["Q"] < table["Q"] or temp["W"] < table["W"] or temp["E"] < table["E"] or temp["R"] < table["R"]):
        #     temp[ s[i] ] += 1
        #     i += 1
        
        # ans = i
        # temp[s[i]] -= 1
        # i -= 1

        ans = len(s)
        for i in range( len(s) ):
            
            # while i < len(s) and (temp["Q"] < table["Q"] or temp["W"] < table["W"] or temp["E"] < table["E"] or temp["R"] < table["R"]):
            #     temp[ s[i] ] += 1
            #     i += 1
            temp[ s[i] ] += 1

           # remove the left part
            while left < len(s) and temp[ s[left] ] > table[ s[left] ]:
                temp[ s[left] ] -= 1
                left += 1

            if temp["Q"] >= table["Q"] and temp["W"] >= table["W"] and temp["E"] >= table["E"] and temp["R"] >= table["R"]:
                ans = min(ans, i - left + 1)
        
        return ans
