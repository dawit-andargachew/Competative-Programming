class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()

        size = len(arr)
        removed_index = int (size * 0.05)
        
        arr = arr[removed_index : size - removed_index ]

        mean = sum(arr)/ len(arr)

        return mean