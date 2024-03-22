class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = count = max_val = 0
        for right in range( len(s) ):
            count += abs( ord(s[right]) - ord(t[right]) )
            while count > maxCost and left < len(s):
                count -= abs( ord(s[left]) - ord(t[left]) )
                left += 1
            max_val = max( max_val, right - left + 1)

        return max_val
        