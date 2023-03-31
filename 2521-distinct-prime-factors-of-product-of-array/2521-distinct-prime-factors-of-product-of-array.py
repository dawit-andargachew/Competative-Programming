class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        # return the prime factors of a number
        def Factorizer( n ):

            factors, i  = set(), 2
            while i * i <= n:
                while n % i == 0:
                    factors.add(i)
                    n //= i
                i += 1
            
            if n > 1:
                factors.add(n)            
            return factors

        product = set()
        # iterate overeach number and combine each prime factor with one another
        for i in nums:
            product = product.union(Factorizer(i))
            # product *= i
           
        return len(product)