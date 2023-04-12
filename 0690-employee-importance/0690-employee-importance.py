"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        # here is a DFS problem so put the data in adjacency list and make dfs on it
        
        graph = defaultdict(list)
        for e in employees:
            graph[e.id].append(e.importance)
            graph[e.id].append(e.subordinates)
        
        Importance = 0
        def dfs( emp ):
            nonlocal Importance

            Importance += graph[emp][0]
            for employee in graph[emp][1]:
                dfs(employee)
        dfs(id)

        return Importance