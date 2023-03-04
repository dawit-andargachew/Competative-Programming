class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join( c for c in s if c.isalnum())
        s = s.lower()

        temp = s
        s = s[::-1]
        
        if s == temp:
            return True
        else:
            return False