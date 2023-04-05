class Solution:
    def splitString(self, s: str) -> bool:
        
        # this question is simila with 306. Additive Number
        curr = []
        def backtack(idx):
            
            if idx >= len(s):
                return len(curr) >= 2
            
            for i in range(idx, len(s)):
                val = int(s[idx:i + 1])
                
                if len(curr) == 0 or val == curr[-1] - 1:
                    curr.append(val)                    
                    if backtack(i + 1):
                        return True
                    curr.pop()
                    
        
        return backtack(0)                
        