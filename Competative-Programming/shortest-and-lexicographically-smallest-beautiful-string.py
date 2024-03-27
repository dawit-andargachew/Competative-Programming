class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        ans = "1" * 101
        left = one = 0
        for i in range( len(s) ):
            if s[i] == '1':
                one += 1
            
            while one >= k:

                # size
                if i - left + 1 < len(ans):
                    ans = s[left: i + 1]
                elif i - left + 1 == len(ans):
                    ans = min(ans, s[left: i + 1])
                
                if s[left] == '1':
                    one -= 1
                left += 1

        return ans if ans != "1" * 101 else ""
        