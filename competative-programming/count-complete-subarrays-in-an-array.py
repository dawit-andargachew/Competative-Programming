class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        ans = 0
        left, right = 0, 0
        uniq = len(set(nums))
        table = defaultdict(int)

        while right < len( nums ):
            table[ nums[right ]] += 1

            while len(table ) == uniq:
                table[ nums[left ]] -= 1
                if table[ nums[left] ] == 0:
                    table.pop( nums[left] )
                
                left += 1
            
            right += 1
            ans += left

        return ans