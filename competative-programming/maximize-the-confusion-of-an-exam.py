class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        n = len(answerKey)
        T_count = F_count = right = 0
        T_left = F_left = max_val = 0

        while right < n:
            if answerKey[right] == "F":
                F_count += 1
            if answerKey[right] == "T":
                T_count += 1
            
            while T_count > k and F_left < n:
                if answerKey[ F_left ] == "T":
                    T_count -= 1
                F_left += 1
            
            while F_count > k and T_left < n:
                if answerKey[ T_left ] == "F":
                    F_count -= 1
                T_left += 1
    
            max_val = max(max_val, right - F_left + 1, right - T_left + 1)
            right += 1
        
        return max_val
        