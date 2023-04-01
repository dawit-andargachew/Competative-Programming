class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxBitwiseOR = 0

        # the maximum bitwise OR is the OR of all elements
        for n in nums:
            maxBitwiseOR |= n
        
        # returns the bitwise OR of all elements on the accumulator
        def giveOR():
            val = 0
            for v in acc:
                val |= v
            return val

        acc, counter = [], 0
        def backtrack(idx):
            nonlocal counter

            if len(acc) > 0:
                if giveOR() == maxBitwiseOR:
                    counter += 1

            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                acc.append( nums[i] )
                backtrack(i + 1)
                acc.pop()
        
        backtrack(0)           

        return counter