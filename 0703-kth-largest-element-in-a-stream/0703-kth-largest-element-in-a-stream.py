class KthLargest:
    # lets use min heap, every time we add a new element 
    # add to the heap and preserve the heap order property
    # so the first element will be the kth-smallest element
    def __init__(self, k: int, nums: List[int]):
        self.nums = heapq.nlargest(k, nums) 
        self.k = k
        
    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heapify(self.nums)
        if len(self.nums) == self.k:
            return self.nums[0]
        else:
            heapq.heappop(self.nums)
            return self.nums[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)