class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def get_sum(n):
            total = 0
            for i in nums:
                total += math.ceil( i / n)

            return total

        # to find the smallest divisor, set low and high values and apply binary search based on the divisor sum we get
        # l = 1, since it is the smallest divisor
        # high = max(nums)
        l, h = 1 , max(nums)
        divisor = 0

        while l <= h:

            mid = ( l + h)//2
            
            
            divisor_sum = get_sum( mid )
            # check the right part if divisor_sum is greater than threshold
            if divisor_sum > threshold:
                l = mid + 1
            else:
                divisor = mid
                h = mid - 1
            

        return divisor