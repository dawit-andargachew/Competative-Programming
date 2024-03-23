class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        table = Counter(text)
        temp = defaultdict(int)
        max_val = left = 0

        for i in range( len(text) ):
            
            temp[ text[i] ] += 1
            h, s = max(temp, key=temp.get), min(temp, key=temp.get)

            # condition one
            while len(temp) > 2 and left < i:
                temp[ text[left] ] -= 1
                if temp[ text[left] ] == 0:
                    del temp[ text[left] ]
                left += 1

            # condition two - while both have frequency > 2
            while len(temp) > 1 and min(temp.values()) > 1 and left < i:
                temp[ text[left] ] -= 1
                if temp[ text[left] ] == 0:
                    temp.pop( temp[left] )
                left += 1
            
            if h in temp and table[h] == temp[h] and len(temp) > 1:
                temp[ text[left] ] -= 1
                if temp[ text[left] ] == 0:
                    temp.pop( text[left] )
                left += 1
            else:
                max_val = max(max_val, i - left + 1)

        return max_val
        