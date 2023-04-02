class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        validPrimes, min_primes = [], [-1, -1]
        
        def generatePrimes():
            primes = [True] * (right + 1)
            primes[0] = primes[1] = False

            # Generate all possible primes from 0 to right
            i = 0
            while i <= right:
                if primes[i]:
                    j = 2 * i
                    while j <= right:
                        primes[j] = False
                        j += i
                i += 1
            
            # select the primes in the range left and right
            for index in range(left, len(primes)):
                if primes[index]:
                    validPrimes.append(index)

        # call the function to generate possible primes
        generatePrimes()

        # select primes with minimum difference
        diff = float('inf')
        for i in range(1, len(validPrimes)):
            curr = validPrimes[i] - validPrimes[i - 1]
            if curr < diff:
                min_primes = validPrimes[i - 1], validPrimes[i]
                #distance of 2 and 1 is the minimum distance that we can have
                if curr <= 2:
                    return min_primes

                diff = curr
        
        return min_primes