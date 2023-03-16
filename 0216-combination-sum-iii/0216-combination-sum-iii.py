class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans, acc = [], []

        def backtrack(idx):
            
            # base cases
            if len(acc) == k and sum(acc) == n:
                ans.append(acc[:])
                return
            
            if len(acc) > k or idx > 9:
                return
            
            # to pick only unique elements iterate from idx to 9
            for i in range(idx, 9 + 1):
                acc.append(i)
                backtrack(i + 1)
                acc.pop()

        # the only valid numbers are 1 to 9, so pass 1
        backtrack(1)

        return ans