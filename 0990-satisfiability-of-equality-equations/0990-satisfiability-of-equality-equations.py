class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # we can use union find by putting all letters connected by '==' together
        # so letters connected by '!=' shouldn't have the same representative
        # step-1: put '==' together
        # step-2: check for '!=' later
        representative = {}
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            representative[y_rep] = x_rep
        
        def find(x):

            if x not in representative:
                representative[x] = x
                return x

            while x != representative[x]:
                x = representative[x]
            return x
        
        # put all '==' on the representative
        for e in equations:
            if e[1] == '=':
                union( e[0], e[3])
        
        # check for '!=', if it doesn't meet  return False
        for e in equations:
            if e[1] == '!':
                if find(e[0]) == find(e[3]):
                    return False
        
        return True