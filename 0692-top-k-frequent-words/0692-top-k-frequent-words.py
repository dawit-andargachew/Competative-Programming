class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # lets use heapify to make it more efficient
        # [[-freq, word]], make frequency negative and take the first K smallest numbers which are the top largest
        
        # store the frequency of each word
        counter = Counter(words)

        # store each [freq, word] pair and make freq negative
        heap = [ [-freq, key] for key, freq in counter.items() ]

        # heapify each words with its frequency, if frequency are equal it will consider words they have
        heapify(heap)
        
        # grab the first k elements from the array
        return [heappop(heap)[1] for _ in range(k)]