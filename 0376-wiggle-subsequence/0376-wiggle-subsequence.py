class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        pos = [1 for _ in range(len(nums))]
        neg = [1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                pos[i] = neg[i-1]+1
                neg[i] = neg[i-1]
            elif nums[i]<nums[i-1]:
                neg[i] = pos[i-1]+1
                pos[i] = pos[i-1]
            else:
                neg[i] = neg[i-1]
                pos[i] = pos[i-1]
                
        return max(pos[-1],neg[-1])