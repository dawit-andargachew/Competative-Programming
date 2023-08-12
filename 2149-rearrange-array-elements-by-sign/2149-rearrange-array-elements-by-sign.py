class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        positive, negative = [], []
        
        #identify positive and negative
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        

        # put positive on even indexes
        for i in range(len(positive)):
            nums[i * 2] = positive[i]
        
        # put negative on odd indexes
        for i in range(len(negative)):
            nums[(i*2) + 1] = negative[i]
            
        return nums