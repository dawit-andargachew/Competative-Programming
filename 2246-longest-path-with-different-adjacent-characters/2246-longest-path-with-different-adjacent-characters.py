class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        for idx, value in enumerate(parent):
            graph[value].append(idx)

        answer = 0
        
        # at each node we need to do 2 things
        # 1, return the laragest single line path two parent
        # 2, consider only two child paths and update the global max
        
        def dfs(node):
            nonlocal answer

            firstBranch, secondBranch = 0, 0
            for child in graph[node]:
                pathLength = dfs(child)
                
                if s[child] != s[node]:
                    if pathLength > firstBranch:
                        secondBranch = firstBranch
                        firstBranch = pathLength
                    elif pathLength > secondBranch:
                        secondBranch = pathLength
            
            # take the two larges paths, and check with global max
            answer = max(answer, firstBranch + 1 + secondBranch)
            
            # 1, return only the largest single path to the parent
            return firstBranch + 1
        
        dfs(0)
        return answer