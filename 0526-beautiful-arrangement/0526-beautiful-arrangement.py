class Solution:
    def countArrangement(self, n: int) -> int:
        
        # it is a backtracking but needs some optimization, Thing about the prunnig case
        # If one of the indices fail to meeet the condition prune the path
        acc, result = [], 0
        def backtrack(idx):
            nonlocal result

            if len(acc) == n:
                result += 1
                    
            if idx > n + 1:
                return 

            for i in range(1, n + 1):
                
                index = len(acc) + 1
                # prunning case, 
                # If one of the indices fail to meet prune the path 
                # i = n + 1 help to prune the path and look for other altenatives
                if not(i % index == 0 or index % i == 0):
                    i = n + 1 # exit from the for loop
                elif i not in acc:
                    acc.append(i)
                    backtrack(i + 1)
                    acc.pop()
        
        backtrack(1)

        return result