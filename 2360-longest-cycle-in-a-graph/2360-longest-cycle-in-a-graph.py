class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        def get_cycle_length(node, edges):
            visited = set()
            while node not in visited:
                visited.add(node)
                node = edges[node]
            return len(visited)

        unvisited = set([i for i in range(len(edges))])
        max_count = -1

        while unvisited:
            cur = unvisited.pop()
            current_visited = {cur}
            while cur not in unvisited:
                cur = edges[cur]
                if cur in current_visited:
                    max_count = max(max_count,get_cycle_length(cur,edges))
                    break
                if cur not in unvisited:
                    break
                unvisited.remove(cur)
                current_visited.add(cur)
                
        return max_count