class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        acc = []

        def backtrack(idx):

            #doesn't need any condition all of them are valid candidates
            ans.append(acc[:])
            
            if idx >= len(nums):
                return

            # valid candidates
            for i in range(idx, len(nums) ): 
                acc.append( nums[i] )
                backtrack(i + 1)
                acc.pop()

        backtrack(0)
        return ans
# SEE ALSO THE CODE BELOW HERE WITHOUT PRUNNING

# with out prunning generate all posible outcomes and check the condition 

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         acc = []

#         def backtrack(i):
#             # valid candidates
#             if i == len(nums):
#                 ans.append(acc[:])
            
#             if i >= len(nums):
#                 return

#             # generate possible candidates
#             acc.append( nums[i] )
#             backtrack(i + 1)
#             acc.pop()
#             backtrack(i + 1)

#         backtrack(0)
#         print(ans)
#         return ans