class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def rever(st):
            return st[::-1]
        
        def inver(st):
            temp = []
            for i in range( len(st) ):
                if st[i] == "0":
                    temp.append("1")
                else:
                    temp.append("0")
            return "".join(temp)
        
        def recur(n):
            if n == 1:
                return "0"
            
            sub = recur(n - 1)
            
            if len(sub) >= k:
                return sub
            else:
                return sub + "1" + rever( inver( sub ))
        
        a = recur(n)

        return a[k-1]