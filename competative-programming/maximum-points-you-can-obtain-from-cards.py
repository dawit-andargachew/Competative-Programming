class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total, n = sum( cardPoints ), len( cardPoints )
        left, right = 0, 0
        
        sub = 0
        min_val = total
        while right < n:
            sub += cardPoints[ right ]

            if right - left == n - k - 1:
                min_val = min(min_val, sub)
                sub -= cardPoints[ left ]
                left += 1
            
            right += 1

        if k == n:
            return total
            
        return total - min_val