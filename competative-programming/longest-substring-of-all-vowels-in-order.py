class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        table = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        left = right = ans = 0

        while right < len( word ):
            
            is_there_e = False # make sure there is `e`-> take this "aiooooouuu"; it meight get skipped
            
            # get the beginning -> move left till `a`
            while left + 1 < len(word) and word[left] != 'a':
                left += 1
            
            # check wheather the elemens are consecutive
            right = left + 1            
            while right + 1 < len(word) and ( table[ word[right] ] == table[ word[right + 1] ] \
                 or table[word[right]] == table[word[right + 1]] - 1):
                 if not is_there_e and word[right] == 'e':
                    is_there_e = True
                 right += 1
            
            if is_there_e and left < len(word) and right < len(word) and  word[left] == 'a' and word[right] == 'u':
                ans = max(ans, right - left + 1)

            left, right = right, right + 1
        
        # a,e,i,o,u
        return ans if ans > 4 else 0