class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        size = len(A)
        
        if size == 1:
            return A[0][0]
        
        for y in range( 1, size):
		
            for x in range( size ):
                min_prev = A[y-1][x] 
                
                if x > 0:
                    min_prev = min( min_prev, A[y-1][x-1] )
                
                if x < size-1:
                    min_prev = min( min_prev, A[y-1][x+1] )
                A[y][x] = A[y][x] + min_prev
                
        return min( A[size-1] )