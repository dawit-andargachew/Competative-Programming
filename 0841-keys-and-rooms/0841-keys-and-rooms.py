class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # traverser every node from 0 and 
        #if len(visited) == len(rooms), all rooms are visited
        visited = set()
        def dfs(node):
            visited.add(node)
            for i in rooms[node]:
                if i not in visited:
                    dfs(i)

        
        #call the dfs from 0
        dfs(0)

        # check number of visited nodes
        return len(visited) == len(rooms)