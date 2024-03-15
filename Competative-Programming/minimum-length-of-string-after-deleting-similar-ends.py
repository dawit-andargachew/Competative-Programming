class Solution:
    def minimumLength(self, s: str) -> int:
        
        low, high = 0, len(s) - 1

        while low < high and s[low] == s[high]:
            # move left suffix
            while low + 1 < high and s[low] == s[low + 1]:
                low += 1

            # move right suffix
            while high - 1 > low and s[high] == s[high - 1]:
                high -= 1
            low += 1
            high -= 1

        return high - low + 1

        