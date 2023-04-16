class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # This problem is somehow bruteforce and n is low <= 100, it may not say TLE
        # The solution is to check maximum number of connected nodes in a graph by considering there distance

        # to check the next bomb detonated or not,
        #   - the area is circular, so d = sqrt( x^2 + y^2) determines the existance of edges
        #   - do this for every nodes which are connected to the first detonated bomb
        #   - since the goal is to maximize the total number of connected nodes in a graph check this for every node
        
        maxDetonated = 0
        def dfs(node, visited):
            nonlocal maxDetonated

            visited.add(node)
            # check the maximum length after adding a node
            maxDetonated = max(maxDetonated, len(visited))

            for i in range( len(bombs) ):                
                if i not in visited:
                    # calculate the distane check with the node coverage are
                    distance = math.sqrt( (bombs[node][0] - bombs[i][0])**2 + (bombs[node][1] - bombs[i][1])**2 )
                    if distance <= bombs[node][2]:
                        dfs(i, visited)
        
        # this for loop checks for every node, so it is bruteforce approach
        for i in range( len(bombs)):
            dfs(i, set())

            # maximum number of detonated bombs is len(bombs), so prune the rest
            if maxDetonated == len(bombs):
                return maxDetonated

        return maxDetonated