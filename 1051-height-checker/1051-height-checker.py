class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        
        indices = 0
        
        for i in range( len(heights) ):
            if heights[i] != expected[i]:
                indices += 1
        
        return indices
        