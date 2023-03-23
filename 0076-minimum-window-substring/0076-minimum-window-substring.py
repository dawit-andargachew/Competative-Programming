class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT, window = {}, {}

        for i in t:
            countT[i] = countT.get(i, 0) + 1
        
        have, need = 0, len(countT)
        sub_str, substrLen = [-1, -1], float('inf')

        l = 0
        for r in range( len(s) ):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] ==  countT[c]:
                have += 1
            
            # there is a substring in s which contain t
            while have == need:
                
                # update the length of substring lenght and  pointers as well
                if ( r - l + 1) < substrLen:
                    sub_str= l, r
                    substrLen = r - l + 1

                window[ s[l] ] -= 1
                if s[l] in countT and window[ s[l]] < countT[ s[l] ]:
                    have -= 1
                    
                l += 1
        

        # return the answer
        left, right = sub_str
        if substrLen != float('inf'):
            return s[left : right + 1]
        else:
            return ""
 
























