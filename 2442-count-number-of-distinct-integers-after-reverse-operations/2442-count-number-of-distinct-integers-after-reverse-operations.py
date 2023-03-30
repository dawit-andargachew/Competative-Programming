class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        reverse = []
        # reverser each number and store in separate list
        for i in nums:

            rev = 0
            while i > 0:
                remainder = i % 10
                rev = rev * 10 + remainder
                i //= 10        
            reverse.append(rev)

        # append it to original list and return number of unique elements   
        nums.extend(reverse)
        
        return len(set(nums))
            