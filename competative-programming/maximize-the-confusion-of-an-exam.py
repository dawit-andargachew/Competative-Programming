class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # assume maximize "T"
        left, right, n = 0, 0, len(answerKey)
        count, max_val = 0, 0

        while right < n:
            if answerKey[right] == "F":
                count += 1
            
            while count > k and left < n:
                if answerKey[ left ] == "F":
                    count -= 1
                left += 1
            max_val = max(max_val, right - left + 1)
            right += 1
        
        # assume maximize "F"
        left = right = count = 0
        while right < n:
            if answerKey[right] == "T":
                count += 1
            
            while count > k and left < n:
                if answerKey[ left ] == "T":
                    count -= 1
                left += 1
            max_val = max(max_val, right - left + 1)
            right += 1

        return max_val
        