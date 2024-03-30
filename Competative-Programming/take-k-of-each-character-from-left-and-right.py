class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        check = Counter(s)
        if check["a"] < k or check["b"] < k or check["c"] < k:
            return -1
        
        # instead of always start from end, start from right the to the end
        # then when add one element from the start, remove one from the end
        # it saves time

        # remove the last elements only
        table = defaultdict(int)
        right = len(s) - 1
        while table["a"] < k or table["b"] < k or table["c"] < k:
            table[ s[right] ] += 1
            right -= 1
        right += 1
        ans =  len(s) - right # initilized by removing the last elements only

        for i in range( len(s) ):
            table[ s[i] ] += 1
            
            # remove right until it doesn't have effect, how?
            while right < len(s) and table[ s[right] ] - 1 >= k:
                table[ s[right] ] -= 1
                right += 1

            # print()
            # print("i ", i,"right ", right)
            # print(table)

            windows_size = i + 1 + len(s) - right
            ans = min(ans, windows_size)

        return ans