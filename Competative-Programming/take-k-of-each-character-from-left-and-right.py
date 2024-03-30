class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0 # no need to remove any elements since k is zero
        temp = Counter(s)
        if temp["a"] < k or temp["b"] < k or temp["c"] < k: # handle exception, we can't have k elements for each
            return -1
        

        # Start by inserting only the last elements and then progressively 
        # add one item from the start, then remove items until k items for `a`,`b`,`c` are present in the map

        # step-1: start by adding only the last elements till k items for each
        table = defaultdict(int)
        right = len(s) - 1
        while table["a"] < k or table["b"] < k or table["c"] < k:
            table[ s[right] ] += 1
            right -= 1
        right += 1

        ans =  len(s) - right # initilized the size by current windows size

        for i in range( len(s) ):
            table[ s[i] ] += 1 # progressively add elements from the start
            
            # remove remove from the right end, until we have k elements for each
            while right < len(s) and table[ s[right] ] - 1 >= k:
                table[ s[right] ] -= 1
                right += 1

            windows_size = i + 1 + len(s) - right
            ans = min(ans, windows_size) # update our answer

        return ans