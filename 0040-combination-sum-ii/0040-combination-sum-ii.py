class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res, curr = [], []
        total = 0

        def backtracking(i):
            nonlocal total

            if total == target:
                res.append(curr[:])
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            total += candidates[i]

            backtracking(i + 1)

            total -= curr[-1]
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtracking(i + 1)

        backtracking(0)
        return res