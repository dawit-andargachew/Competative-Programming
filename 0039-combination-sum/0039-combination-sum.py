class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        acc = []
        total = 0
        
        def backtrack(i):
            nonlocal total
                
            if total == target:
                ans.append(acc[:])
                return

            # prune since it is sorted
            if  i >= len(candidates) or (target - total) < candidates[i]:
                return

            # choose
            acc.append(candidates[i])
            total += candidates[i]
            backtrack(i)

            # not choose
            total -= acc[-1]
            acc.pop()
            backtrack(i + 1)

        candidates.sort()
        backtrack(0)
        return ans

    
# what approach should we use if the number it too large like 10000 - Dynamic Programming