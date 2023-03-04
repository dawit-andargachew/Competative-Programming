class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        left = 0
        right = len(s) - 1
        while( left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            right -= 1
            left += 1
        
                
        res = " ".join(s)
        
        return res
        