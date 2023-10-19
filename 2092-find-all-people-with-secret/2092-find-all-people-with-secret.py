class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = [i for i in range(n)]
        secret_group = {0, firstPerson}
        parent[firstPerson] = 0

        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a

        def union(a, b):
            par_a = find(a)
            par_b = find(b)
            if par_a < par_b:
                parent[par_b] = par_a
            else:
                parent[par_a] = par_b

        meetings.sort(key=lambda x: x[2])
        meeting_groups = []

        last_time = meetings[0][2]
        group = [[meetings[0][0], meetings[0][1]]]

        for meet in meetings[1:]:
            if meet[2] == last_time:
                group.append([meet[0], meet[1]])
            else:
                meeting_groups.append(group)
                group = [[meet[0], meet[1]]]
                last_time = meet[2]
        meeting_groups.append(group)

        for group in meeting_groups:
            for meet in group:
                union(meet[0], meet[1])

            for meet in group:
                if find(meet[0]) != 0:
                    parent[meet[0]] = meet[0]
                    parent[meet[1]] = meet[1]
                else:
                    secret_group.add(meet[0])
                    secret_group.add(meet[1])
                    
        return secret_group