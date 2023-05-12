class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # FOR DFS IMPLEMENTATION SEE PREVIOS SUBMISSION

        # constuct graph and keep track of degree 
        graph, degree = defaultdict(list), [0] * numCourses
        for index, value in enumerate(prerequisites):
            graph[ value[1] ].append( value[0] )
            degree[ value[0] ] += 1

        # if a given course has no prerequisites, its degree becomes zero
        # start BFS from courses which have no prerequisites
        q = deque()
        for i in range( len(degree) ):
            if degree[i] == 0:
                q.append(i)

        # do a BFS, and decrement the degree once we reach a course
        # if degree of a courser is zero it has no prerequisites so add to queue
        order = 0
        while q:
            curr = q.popleft()
            order += 1
            for node in graph[curr]:
                degree[node] -= 1

                if degree[node] == 0:
                    q.append( node )

        # EDGE CASE, what if there is no prerequisites
        if order == numCourses or len(prerequisites) == 0:
            return True
        return False