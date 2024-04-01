class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda x: x[1])
        temp = queries[:] # helps to keep the order of quries
        queries.sort()

        element_map, store = Counter(queries), defaultdict(int)
        left = right = 0

        # loop each query and determine non-requested servers
        for q in range(len(queries)):

            if right < len(logs) and logs[right][1] < queries[q] - x:
                # previos quries value is the currenct minimum range
                # take this 
                '''
                n = 4
                logs = [[4,3],[2,16],[1,21],[3,22],[1,13],[3,10],[2,1],[1,12],[4,13],[2,18]]
                x = 8
                queries = [14,28,29]
                '''
                store.clear()
                left = right

                while left < len(logs) and  logs[left][1] < (queries[q] - x):
                    left += 1
                
                right = left 
                while right < len(logs) and logs[right][1] <= queries[q]:
                    store[ logs[right][0] ] += 1
                    right += 1
                element_map[queries[q]] = n - len(store) # store number of inactive servers
            
            else: # keep a sliding windows, since consecutive quieries are overlapping
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
                element_map[ queries[q] ] = n - len(store) # store number of inactive servers
            
        answer = []
        for i in temp:
            answer.append( element_map[i] )
        return answer