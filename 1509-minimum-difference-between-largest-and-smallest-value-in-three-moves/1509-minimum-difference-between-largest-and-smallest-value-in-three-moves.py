class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        # length <= 4, so the minimum difference becomes zero.
        if len(nums) <= 4:
            return 0
        
        # In total we have 3 moves so lets take every possible move        
        nums.sort()
        
        def allFirst():
            return nums[-1] - nums[3]
        
        def allLast():
            return nums[-4] - nums[0]

        def _1First_2Last():
            return nums[-3] - nums[1]

        def _2First_1Last():
            return nums[-2] - nums[2]
        
        answer = min( allFirst(), allLast(), _1First_2Last(), _2First_1Last() )

        return answer