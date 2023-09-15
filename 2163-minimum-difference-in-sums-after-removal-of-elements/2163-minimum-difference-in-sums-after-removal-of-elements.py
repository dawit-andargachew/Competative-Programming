class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        prefix_q = [-x for x in nums[:n]]
        heapq.heapify(prefix_q)
        
        diff = [0]*(n+1)
        diff[0] = -sum(prefix_q)
        
        for i in range(n):
            r = nums[i+n]        
            greatest = -heapq.heappushpop(prefix_q, -r)
            diff[i+1] = diff[i] - greatest + r
        
        # Min heap
        suffix_q = nums[2*n:]
        heapq.heapify(suffix_q)
        
        prev_sum = sum(suffix_q)
        diff[-1] -= prev_sum
        
        for i in range(n):
            temp = nums[len(nums) - 1 - n - i]            
            smallest = heapq.heappushpop(suffix_q, temp)
            prev_sum = prev_sum - smallest + temp
            diff[n - 1 - i] -= prev_sum 

        return min(diff)