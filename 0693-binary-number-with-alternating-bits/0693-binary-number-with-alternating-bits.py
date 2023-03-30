class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        
        # the goal is to check weather all adjacent bit have different values
        # so iterate over all bits and check them

        prev = 1 & n
        n >>= 1

        while n > 0:
            curr = 1 & n

            if curr ^ prev == 0:
                return False
            
            prev = curr
            n >>= 1
        
        return True