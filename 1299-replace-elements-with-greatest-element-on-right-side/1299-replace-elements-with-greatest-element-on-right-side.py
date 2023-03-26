class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 1:
            return [-1]
        
        i = len(arr) - 1

        # put the last element on its previous 
        prev = arr[i -1]
        arr[i - 1] = arr[i]


        i -= 1
        while i > 0:
            temp = arr[i - 1]
            arr[i -1] = max(prev, arr[i])
            prev = temp
            i -= 1

        arr[-1] = -1

        return arr