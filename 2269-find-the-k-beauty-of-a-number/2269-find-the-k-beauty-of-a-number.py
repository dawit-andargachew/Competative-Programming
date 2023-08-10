class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        high, low, answer = 0, 0, 0

        s = str(num)
        while high < len(s):

            if high - low + 1 == k:
                curr = int( s[low:high + 1])
                
                # check for edge case, when curr == 0
                if curr != 0 and num % curr == 0:
                    answer += 1
                low += 1
            high += 1

        return answer