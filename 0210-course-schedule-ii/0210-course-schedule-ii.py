class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # the question is about two things
        # 1, Cycle Detection on Directed Graph
        # 2, Topological Sort

        # edge case, if there are no prerequisite, return courses in any order
        if len(prerequisites) == 0:
            return [n for n in range(numCourses)]

        graph = defaultdict(list)
        for pre in prerequisites:
            graph[ pre[1] ].append( pre[0])

        # helps to detect the occurence of cycle
        WHITE, GREY, BLACK, color = 0, 1, 2, defaultdict(int)
        def hasCycle(node):
            color[node] = GREY
            for neighbour in graph[node]:
                if color[neighbour] == WHITE:
                    if not hasCycle(neighbour):
                        return False                
                if color[neighbour] == GREY:
                    return False

            color[node] = BLACK
            return True

        # helps to get the topological ordering of nodes        
        visited, order = set(), []
        def TopologicalOrdering(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    TopologicalOrdering(i)            
            order.append(node)           

        # check for cycle for every node in the graph
        for i in range(numCourses):
            if not hasCycle(i):
                return []

        # the graph has no cycle, so return the topological ordering of nodes
        for key in list(graph.keys()):
            if key not in visited:
                TopologicalOrdering(key)

        # what if there are courses that are not listed, so add them in the ordering too
        if len(order) != numCourses:
            # remaining courses are from len(order) to numCoures
            remaining = len(order) 
            order += [i for i in range(remaining, numCourses)]
        
        # the ordering should be topological, so reverse before returning the list
        return order[::-1]