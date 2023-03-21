class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # extract common letters among all words
        common = set(words[0])
        for w in words:
            common = common.intersection( set( w ))
        
        # initialize the frequency of each common letters to large number which is updated later
        map = defaultdict(int)
        for s in common:
            map[s] = float('inf')

        # for each word grab its common letters count and take the minimum among all
        for w in words:
            temp = Counter( w )

            for c in common:
                map[c] = min( map[c], temp[c])

        answer = []
        # populate these common letters with their frequency in to list
        for k,v in map.items():
            while v:
                answer.append( k )
                v -= 1
                
        return answer