class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        maps = collections.defaultdict(dict)

        for (left, right), value in zip(equations, values):
            maps[left][right] = value
            maps[right][left] = 1 / value

        results = []
        for left, right in queries:
            visited = set()
            queue = collections.deque([(left, 1)])  # node and the cost to get here
            res = -1
            while queue:

                node, cost = queue.popleft()
                visited.add(node)
                if right in maps[node]:
                    res = cost * maps[node][right]
                    break
                queue.extend([(neighbor, cost * n_cost) for neighbor, n_cost in maps[node].items() if neighbor not in visited])
            results.append(res)

        return results