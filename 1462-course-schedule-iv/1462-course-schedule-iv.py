class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        adj = [set() for _ in range(n)]
        indegrees = [0] * n
        ancestors = [set() for _ in range(n)]
        for i in range(len(prerequisites)):
            prereq, main = prerequisites[i][0], prerequisites[i][1]
            adj[prereq].add(main)
            indegrees[main] += 1
        
        queue = deque()
        for a in range(len(indegrees)):
            if(indegrees[a] == 0):
                queue.append(a)

        while queue:
            cur_course = queue.pop()
            neighbors = adj[cur_course]
            for neighbor in neighbors:
                indegrees[neighbor] -= 1
                ancestors[neighbor].add(cur_course)
                ancestors[neighbor].update(ancestors[cur_course])
                if(indegrees[neighbor] == 0):
                    queue.append(neighbor)
        
        output = []
        for query in queries:
            prereq2, main2 = query[0], query[1]
            all_prereqs = ancestors[main2]
            if(prereq2 in all_prereqs):
                output.append(True)
                continue
            else:
                output.append(False)
                
        
        return output