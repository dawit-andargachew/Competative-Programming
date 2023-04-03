class Solution:
    def minSteps(self, n: int) -> int:
        
        #******************* It can also solved by summing the prime factors of a number

        # checks if the number is prime or not 
        # if the number is no't prime it retuns maximum divisor as well
        def isPrime_with_largestDivisor(num):
            d, maxDivisor = 2, 1
            while d * d <= num:
                if num % d == 0:
                    maxDivisor = max( maxDivisor, num//d)
                d += 1
            #returns a tuple of [isPrime: boolean, maxDivisor: integer]
            return [maxDivisor == 1, maxDivisor]


        # it is a Dynamic Programming Prolem and here is the method I choose
        # minimum number of operations = memo[largestDivsor] + 1 + number//largestDivisor - 1
        # why? because the largest Divisor can make minimum numbe of operations

        #  here is explanation for every term memo[largestDivsor] + 1 + number//largestDivisor - 1
        #         memo[largestDivsor] => makes minimum possible  operations
        #         ... + 1 => operation to copy memo[largestDivsor]  
        #         ... + number// largestDivisor => operations to fil the rest of the gap
        #         ... -1 => largestDivisor is already filled so skip this part
        # it can be written as 
        #       minimum operations = memo[largestDivsor] + number//largestDivisor

        memo = defaultdict(int)
        memo[1] = 0

        i = 2
        while i <= n:
            check = isPrime_with_largestDivisor(i)
            if check[0]:
                memo[i] = i
            else:
                divisor= check[1]
                memo[i] = memo[divisor] + i//divisor
            i += 1
        
        return memo[n]