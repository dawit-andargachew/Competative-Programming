class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if numOnes >= k:
            return k
        else:
            k -= numOnes            
            if numZeros >= k:
                return numOnes
            else:
                k -= numZeros
                return numOnes - k