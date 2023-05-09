class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # extract the values in to list
        matrix = [element for row in matrix for element in row]
        heapq.heapify(matrix)

        # iterate and remove k elements
        for _ in range(k - 1):
            heapq.heappop(matrix)
        return matrix[0]