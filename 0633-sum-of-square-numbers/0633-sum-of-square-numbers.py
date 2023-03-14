class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        n = []
        # store number <= c, a**2 + b**2 = c
        # so all numbers must be <= c, ignore the rest
        for i in range(c + 1):
            if i*i <= c:
                n.append(i*i)
            else:
                break

        l, r = 0, len(n)-1

        isFound = False
        
        # find two numbers their sum is equal to c
        while l <= r:
            square_sum = n[l] + n[r]
            if square_sum == c:
                isFound = True
                break
            elif square_sum > c:
                r -= 1
            else:
                l += 1

        return isFound