class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        table = defaultdict(int)
        total, max_val = 0, 0
        left, right = 0, 0

        while right < len(nums):
            table[ nums[right] ] += 1
            total += nums[right]

            if table[ nums[right] ] > 1:

                while table[ nums[right] ] > 1:
                    table[ nums[left] ] -= 1
                    total -= nums[left]
                    if table[ nums[left] ] == 0:
                        table.pop( nums[left] )
                    left += 1
            
            max_val = max(max_val, total)            
            right += 1
        
        return max_val