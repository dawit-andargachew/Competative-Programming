class Solution:
    def countPrimes(self, n: int) -> int:
        # edge case
        if n <= 2:
            return 0

        # lets use Sieve of Eratosthenes to find the prime numbers
        is_prime: list[bool] = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False # 0 and 1 are not primes so make them false

        i = 2

        # loop until sqrt(n) to check all prime numbers
        while i * i <= n:

            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
                    
            i += 1

        return sum(is_prime)