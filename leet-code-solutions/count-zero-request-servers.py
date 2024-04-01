class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda x: x[1])
        temp = queries[:]
        queries.sort()

        element_map, store = Counter(queries), defaultdict(int)
        left = right = 0

        # initialize
        while left < len(logs) and  logs[left][1] < (queries[0] - x):
            left += 1
        
        right = left 
        while right < len(logs) and logs[right][1] <= queries[0]:
            store[ logs[right][0] ] += 1
            right += 1
        element_map[queries[0]] = n - len(store)

        # loop each query and determine non-requested servers
        for q in range(1, len(queries)):

            if right < len(logs) and logs[right][1] < queries[q] - x:
                store.clear()
                left = right

                while left < len(logs) and  logs[left][1] < (queries[q] - x):
                    left += 1
                
                right = left 
                while right < len(logs) and logs[right][1] <= queries[q]:
                    store[ logs[right][0] ] += 1
                    right += 1
                element_map[queries[q]] = n - len(store)
            
            else:
                # move left 
                while left < right and logs[left][1] < (queries[q] - x):
                    store[ logs[left][0] ] -= 1
                    if store[ logs[left][0]] == 0:
                        store.pop( logs[left][0] )
                    left += 1
                
                # move right
                while right < len(logs) and logs[right][1] <= queries[q]:
                    store[ logs[right][0] ] += 1
                    right += 1
                element_map[ queries[q] ] = n - len(store)
            
        answer = []
        for i in temp:
            answer.append( element_map[i] )
        return answer