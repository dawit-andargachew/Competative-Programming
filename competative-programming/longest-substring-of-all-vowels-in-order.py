class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        table = defaultdict(int)
        table['a'] = 0
        table['e'] = 1
        table['i'] = 2
        table['o'] = 3
        table['u'] = 4
        
        left = right = ans = 0

        while right < len( word ):
            
            # get the beginning -> move left till a
            while left + 1 < len(word) and word[left] != 'a':
                left += 1
            
            right = left + 1            
            while right + 1 < len(word) and ( table[ word[right] ] == table[ word[right + 1] ] \
                 or table[word[right]] == table[word[right + 1]] - 1):
                 right += 1
            
            if left < len(word) and right < len(word) and word[left] == 'a' and word[right] == 'u':
                temp = left # make sure there is `e`-> take this "aiooooouuu"
                while temp < right and word[temp] != "e":
                    temp += 1
                
                if word[temp] == 'e':
                    ans = max(ans, right - left + 1)

            left = right
            right += 1
        # a,e,i,o,u
        return ans if ans > 4 else 0