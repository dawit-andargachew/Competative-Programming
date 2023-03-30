class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # makeing XOR will exluded similar bits 
        x ^= y
        return x.bit_count()