class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

        ans = []
        q = deque()

        for i in range( len(nums) ):

            while q and nums[q[-1]] < nums[i]:
                q.pop()
                 
            q.append(i)

            if i - k + 1 > q[0]:
                q.popleft()

            if i >= k - 1:
                ans.append( nums[q[0]] )

        return ans