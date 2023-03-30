class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # if len(arr) < 3:
        #     return False
        
        i, peakValue = 1, arr[0]
        while i < len(arr):
            
            # grab the first peak value
            if peakValue > arr[i]:
                break

            if peakValue == arr[i]:
                return False
        
            peakValue = arr[i] # update peakVlaue until we get
            i += 1

        # i == 1 means the peak value is at first index
        # i >= len(arr) means have no peakValue, have no decreasing part
        if i == 1 or i >= len(arr):
            return False
        
        # check weather part of after peakValue is decreasing or not
        while i < len(arr):
            
            if peakValue <= arr[i] or arr[i - 1] <= arr[i]:
                return False
            i += 1


        return True
        