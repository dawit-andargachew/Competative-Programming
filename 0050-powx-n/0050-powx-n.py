class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power_n(x, n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                return power_n( x * x, n//2)
            else:
                return x * power_n(x * x, (n-1)//2 )

        if n == 0 or x == 1:
            return float(1)
        elif n >= 1:
            return power_n(x, n)
        
        else: # if n < 0:
            return 1/power_n(x, abs(n))