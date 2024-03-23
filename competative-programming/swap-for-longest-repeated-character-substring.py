class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        table = Counter(text)
        temp = defaultdict(int)
        max_val = left = 0

        for i in range( len(text) ):
            
            temp[ text[i] ] += 1
            h, s = max(temp, key=temp.get), min(temp, key=temp.get)

            # condition one - if it has more than 3 chars remove till 2 remain
            while len(temp) > 2 and left < i:
                temp[ text[left] ] -= 1
                if temp[ text[left] ] == 0:
                    del temp[ text[left] ]
                left += 1

            # condition two - while both have frequency > 2, remove till one of them have freq of 1
            while len(temp) > 1 and min(temp.values()) > 1 and left < i:
                temp[ text[left] ] -= 1
                if temp[ text[left] ] == 0:
                    temp.pop( temp[left] )
                left += 1
            
            '''
            `h in temp` seems unnecessary since `temp` is defaultdict, what if h is removed in the above while
            loops? So `h in temp` prevents new elements from inserting with freq of 1 and make sure not to increase
            the temp size.
            If the temp size is increased, it initiates the above while loops to remove necessary values
            '''
            if h in temp and table[h] == temp[h] and len(temp) > 1:
                temp[ text[left] ] -= 1
                if temp[ text[left] ] == 0:
                    temp.pop( text[left] )
                left += 1
            else:
                max_val = max(max_val, i - left + 1)

        return max_val
        