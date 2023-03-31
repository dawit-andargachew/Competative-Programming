class Solution:
    def findGCD(self, nums: List[int]) -> int:

        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a % b)

        nums.sort()
        return  GCD(nums[0], nums[-1])