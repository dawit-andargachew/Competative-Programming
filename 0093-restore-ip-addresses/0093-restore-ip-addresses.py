class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # edge cases, len(s) should be between 4 and 12
        if len(s) < 4 or len(s) > 12:
            return []
        
        result, acc = [], []
        dots = [0] # make it array enalbe us to access inside nested function easily and count the number of dots
        def backtrack(idx):

            if dots[0] == 4 and idx == len(s):
                acc[-1] = acc[-1][:-1] # remove the last dot
                result.append( ''.join(acc[:]) )
                return

            for i in range(idx, min( idx + 3, len(s))):
                
                # check whether the move is valid or not
                if int(s[idx:i + 1]) < 256 and (idx == i or s[idx] != '0'):
                    
                    acc.append(s[idx: i + 1] + ".")
                    dots[0] += 1

                    backtrack(i + 1)
                    
                    acc.pop()
                    dots[0] -= 1
        backtrack(0)
            
        return result