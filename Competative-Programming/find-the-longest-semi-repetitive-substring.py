class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        ans = 1
        pair = left = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                pair += 1
            
            while pair > 1 and left < i:
                if s[left] == s[left + 1]:
                    pair -= 1
                left += 1
        
            ans = max(ans, i - left + 1)

        return ans