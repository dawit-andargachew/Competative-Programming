class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_count = [0 for _ in range(len(quiet))]
        graph = defaultdict(list)
        answer = [idx for idx in range(len(quiet))]
        
        for rich, poor in richer:
            graph[rich].append(poor)
            richer_count[poor] += 1
            
        queue = collections.deque([])
        for person, rich_count in enumerate(richer_count):
            if not rich_count:
                queue.append(person)
                
        while queue:
            person = queue.popleft()
            quieter_person = answer[person]
            
            for poorer in graph[person]:
                quieter_richer = answer[poorer]
                answer[poorer] = min(quieter_person, quieter_richer, key = lambda prsn : quiet[prsn])
                richer_count[poorer] -= 1
                if not richer_count[poorer]:
                    queue.append(poorer)
        return answer