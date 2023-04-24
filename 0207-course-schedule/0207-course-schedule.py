class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # the question is simply check for cycle
        WHITE, GREY, BLACK = 0, 1, 2 # not visited, on progress, visited respectively

        preMap = defaultdict(list)
        for pre in prerequisites:
            preMap[pre[0]].append( pre[1] )            
        
        color = defaultdict(int)
        def hasCycle(node):

            color[node] = GREY
            for neighbour in preMap[node]:
                if color[neighbour] == WHITE:
                    if not hasCycle(neighbour):
                        return False
                # if the next explored node is still explored there is a cycle
                elif color[neighbour] == GREY: 
                    return False

            # after visiting all of 'node' neighbours mark it as done.
            color[node] = BLACK
            return True

        for course in range( numCourses ):
            if not hasCycle(course):
                return False

        return True        