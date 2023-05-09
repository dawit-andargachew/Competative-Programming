class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        # lets use heap
        # heapify is minheap => convert nums to negative
        # store half and total before converting to negative and decrement
        # total until is half
        counter, total = 0, sum(nums)
        half = total/2
        nums = [-i for i in nums]

        heapq.heapify(nums)
        while total > half:
            counter += 1
            num = heapq.heappop(nums)
            num = num/2
            total += num
            heapq.heappush(nums, num)

        return counter