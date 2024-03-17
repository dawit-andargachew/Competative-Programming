class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        table, n = defaultdict(int), len(nums)
        for i in nums:
            table[i] += 1

        freq = defaultdict(int)
        left, right = 0, 0
        ans = 0

        while right < n:
            while right < n:
                freq[ nums[right] ] += 1
                right += 1

                if len(freq) == len(table):
                    ans += 1
                    break
                
            # check weather other combination exist starting from zero
            temp = freq.copy()
            left = 0
            while left < right:
                freq[nums[left]] -= 1

                if freq[ nums[left] ] == 0:
                    freq.pop( nums[left] )
                
                if len( freq ) == len( table ):
                    ans += 1
                left += 1
                
            freq = temp

        return ans