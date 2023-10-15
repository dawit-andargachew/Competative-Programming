class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = collections.defaultdict(list)
        for i in range(len(edges)):
            [src, dest] = edges[i]
            d[src].append((dest, succProb[i]))
            d[dest].append((src, succProb[i]))
        probability = [0]*n
        probability[start] = 1

        q = deque()
        q.append((start, 1))
        while q:
            node, prob = q.popleft()
            for [n,p] in d[node]:
                p *= prob
                if p > probability[n]:
                    probability[n] = p
                    q.append((n,p))
        return probability[end]