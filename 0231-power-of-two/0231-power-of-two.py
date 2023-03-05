class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 1:
            return True

        elif  n <= 0 or n % 2 == 1:
            return False
        
        return self.isPowerOfTwo( n//2)