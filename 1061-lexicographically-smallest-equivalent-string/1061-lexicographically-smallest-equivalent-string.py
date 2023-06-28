class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        # initialize representative dict, 
        representative = {}

        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            
            # to make it lexicographically smallest check the reps
            if x_rep >= y_rep:
                representative[ x_rep ] = y_rep
            else:
                representative[ y_rep ] = x_rep
        
        def find(val):
            if val not in representative:
                representative[val] = val
                return val

            while val != representative[val]:
                val = representative[val]
            return val
        

        for i in range( len(s1) ):
            union( s1[i], s2[i])
        
        # extract lexicographically smallest equivalent string for baseStr
        answer =  []
        for i in baseStr:
            # for each char find its representative
            answer.append(find(i))

        return "".join(answer)