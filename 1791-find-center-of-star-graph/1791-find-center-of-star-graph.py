class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        # lets find the intersection of every list
        # because there is exaclty one star node
        answer = set(edges[0])
        for e in edges:
            answer = answer.intersection(set(e))
            
        
        return list(answer)[0]