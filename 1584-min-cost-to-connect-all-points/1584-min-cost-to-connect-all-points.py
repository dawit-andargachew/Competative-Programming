class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, edges = len(points), []
        for i in range(n):
            for j in range(i+1,n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1]) 
                edges.append((d,i,j))
        
    
        edges.sort()
        parent = [x for x in range(n)]
        res, count = 0, 0
        for d,u,v in edges:

            if count == n-1:
                break

            if self.union(u,v,parent):
                res += d
                count += 1
            
        return res 
    
    def find(self,x,parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x],parent)
        return parent[x]
    
    def union(self,x,y,parent):
        px = self.find(x,parent)
        py = self.find(y,parent)

        if px != py:
            parent[px] = parent[py]
            return True

        return False