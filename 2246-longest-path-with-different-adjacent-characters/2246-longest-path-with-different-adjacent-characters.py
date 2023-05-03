class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        for idx, value in enumerate(parent):
            graph[value].append(idx)

        answer = 0
        
        # at each node we need to do 2 things
        # 1, take the two largest paths and update the global max
        # 2, return the firstLargest + 1 to the parent
        
        def dfs(node):
            nonlocal answer

            firstLongest, secondLongest = 0, 0
            for child in graph[node]:
                pathLength = dfs(child)
                
                # check adjacent nodes are different => parent and child
                if s[child] != s[node]:
                    if pathLength > firstLongest:
                        secondLongest = firstLongest
                        firstLongest = pathLength
                    elif pathLength > secondLongest:
                        secondLongest = pathLength
            
            # take the two larges paths, and check with global max
            answer = max(answer, firstLongest + 1 + secondLongest)
            
            # return the largest single path to the parent
            return firstLongest + 1
        
        dfs(0)
        return answer