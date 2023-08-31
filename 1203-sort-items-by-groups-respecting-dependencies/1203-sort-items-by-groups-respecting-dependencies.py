class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
       
        item_to_group_map, graph_group = {}, {}
        indegree_group, group_topo_order = {}, {}
        new_group_id = m

        for i, group_id in enumerate(group):
            if group_id == -1:
                item_to_group_map[i] = new_group_id
                graph_group[new_group_id] = set()
                group_topo_order[new_group_id] = []
                indegree_group[new_group_id] = 0
                new_group_id+=1
            else:
                item_to_group_map[i] = group_id
                graph_group[group_id] = set()
                group_topo_order[group_id] = []
                indegree_group[group_id] = 0

        graph_vertices = {i: set() for i in range(n)}
        indegree_vertices = {i: 0 for i in range(n)}
        for i, before_item in enumerate(beforeItems):
            for vertice in before_item:
                graph_vertices[vertice].add(i)
                indegree_vertices[i]+=1

                item_group = item_to_group_map[i]
                before_item_group = item_to_group_map[vertice]
                if item_group != before_item_group and item_group not in graph_group[before_item_group]:
                    graph_group[before_item_group].add(item_group)
                    indegree_group[item_group]+=1

        def get_topological_order(graph_vertices, indegree_vertices):
            que = deque([])
            order = []
            for key, value in indegree_vertices.items():
                if value == 0:
                    que.append(key)

            while len(que):
                vertex = que.popleft()
                order.append(vertex)
                for v in graph_vertices[vertex]:
                    indegree_vertices[v]-=1
                    if indegree_vertices[v] == 0:
                        que.append(v)
            return order
        vertice_order = get_topological_order(graph_vertices, indegree_vertices)
        if len(vertice_order) != n:
            return []

        for item in vertice_order:
            group_topo_order[item_to_group_map[item]].append(item)

        group_order = get_topological_order(graph_group, indegree_group)
        if len(group_order) != len(graph_group):
            return []

        final_vertice_order = []
        for group in group_order:
            final_vertice_order.extend(group_topo_order[group])
            
        return final_vertice_order