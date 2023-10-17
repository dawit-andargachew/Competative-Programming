class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        bestOverlap = 0
        i1, i2 = [], []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    i1.append((r, c))

                if img2[r][c] == 1:
                    i2.append((r, c))

        overlap = {}
        for i1_r, i1_c in i1:
            for i2_r, i2_c in i2:
                shift = (i2_r - i1_r, i2_c - i1_c)
                overlap[shift] = overlap.get(shift, 0) + 1
                bestOverlap = max(bestOverlap, overlap[shift])
        
        return bestOverlap