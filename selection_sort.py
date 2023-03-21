class Solution: 
    def select(self, arr, i):
        # code here
        minNum = i
        for j in range(i, len(arr)):
            if arr[minNum] > arr[j]:
                minNum = j
        return minNum
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minIndex = self.select(arr, i)
            
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
