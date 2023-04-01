class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a%b)

        # here is a  bruteforce approach to find GCD
        count = 0
        for i in range( len(nums) ):
            temp = nums[i]
            for j in range(i, len(nums) ):
                temp = GCD(temp, nums[j])

                if temp == k:
                    count += 1
                    
                # the GCD is affected by the minimum value, so prone this one and move to the next choice
                elif temp < k: 
                    break


        return count