class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        answer, acc = [], [0] #we start from node 0, so hardcode it before starting dfs

        # lets apply dfs on the graph and keep track visited nodes 
        # like backtracking when the last element is n - 1 => len(graph) - 1, store the path
        visited = set()
        def dfs_with_backtrack(node):

            # if node == le(graph) - 1 => the last node is reached so store it
            if node == len(graph) - 1:
                answer.append(acc[:])

            for i in graph[node]:
                if i not in visited:
                    acc.append(i) # append before calling backtack
                    dfs_with_backtrack(i)
                    acc.pop() # remove after visiting

        dfs_with_backtrack(0)

        return answer