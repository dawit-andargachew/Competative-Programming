class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        a, b = 0, 0
        for i in nums:
            a = ( a ^ i) & ~ b
            b = ( b ^ i) & ~ a
        
        return a