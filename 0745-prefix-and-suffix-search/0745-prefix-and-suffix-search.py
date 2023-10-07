class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix = {}
        for idx, word in enumerate(words):
            cur = self.prefix
            for letter in word:
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            # store data somehow
            cur['idx'] = [idx, word]
                

    def f(self, prefix: str, suffix: str) -> int:
        possible = []
        cur = self.prefix
        for letter in prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        # BFS to find all possible words
        cur_layer = [cur]
        while len(cur_layer) != 0:
            next_layer = []
            for i in range(len(cur_layer)):
                for letter in cur_layer[i]:
                    if letter != 'idx':
                        next_layer.append(cur_layer[i][letter])
                    elif cur_layer[i]['idx'][1].endswith(suffix):
                        possible.append(cur_layer[i]['idx'][0])
            cur_layer = next_layer
        if len(possible) == 0:
            return -1
        return max(possible)
            
    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)```
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)