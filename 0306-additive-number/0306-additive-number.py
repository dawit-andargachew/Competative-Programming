class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        
        # similar to 1849. Splitting a String Into Descending Consecutive Values
        # But in here the the number can't have leading zero

        acc = []
        def backtrack(idx):

            if idx >= len(s):
                return len(acc) >= 3

            for i in range(idx, len(s)):

                currVal = s[idx:i + 1]
                # here is the edge case, the number can't have leading zero
                # so check this condition here
                if len(currVal) > 1 and currVal[0] == '0':
                    i = len(s)
                    continue
                
                val = int(currVal)
                if len(acc) <= 1 or val == acc[-1] + acc[-2]:
                    acc.append(val)
                    if backtrack(i + 1):
                        return True
                    acc.pop()
        
        return backtrack(0)