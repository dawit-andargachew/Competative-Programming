class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        acc = []
        
        def backtrack(i):
            total = sum(acc)
            if total > target or i > len(candidates):
                return
            if total == target:
                ans.append(acc[:])
                return

            for idx in range(i, len(candidates)):
                acc.append(candidates[idx])
                backtrack(idx)
                acc.pop()

        backtrack(0)
        return ans