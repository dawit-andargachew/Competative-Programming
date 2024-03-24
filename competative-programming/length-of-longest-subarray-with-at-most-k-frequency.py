class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        table = defaultdict(int)
        left = ans = 0

        for idx, val in enumerate( nums ):
            table[ val ] += 1

            while table[ val ] > k and left < idx:
                table[ nums[left] ] -= 1

                # if table[ nums[left] ] == 0:
                #     table.pop(nums[left])
                
                left += 1

            ans = max(ans, idx - left + 1)

        return ans
        