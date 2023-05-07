#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,heap, current):
        # code here
        # heapify down by removing element
        while heap[(current - 1)//2] > heap[current] and current > 0:
            heap[(current - 1)//2], heap[current] = heap[current], heap[(current - 1)//2]
            current = (current - 1)//2
    
    #Function to build a Heap from array.
    def buildHeap(self,arr, current, limit):
        # code here
        # heapify up by adding element
        left, right = 2*current + 1, 2*current + 2

        while current < limit and left < limit and arr[current] > arr[left] or right < limit and arr[current] > arr[right]:
            if arr[left] < arr[right]:
                arr[current], arr[left] = arr[left], arr[current]
                current = left
            else:
                arr[current], arr[right] = arr[right], arr[current]
                current = right
    
            left, right = current*2 + 1, current*2 + 2
    
    #Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        
        # arr = [-]
        # build heap here just by shifting element to the heapify methods
        for i in range(len(arr)):
            arr[i] = -1* arr[i]
            self.heapify(arr, i)
        # print("after heapify the array is ")
        # print(* arr)
        # like heapify shift the indices by considering the element before it is sorted inplace
        for i in range(len(arr)):
            target = len(arr)-i -1
            arr[0], arr[target] = arr[target], -arr[0]
            # limi
            self.buildHeap(arr, 0, len(arr) - i)
            
        # print("the array is ")
        # print(*arr)
        #code here

