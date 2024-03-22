class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        odd_c = even_c = max_val = 0
        for i in range( len(arr) ):
            # odd turbulent
            if (i % 2 == 1 and i + 1 < len( arr ) and arr[i] > arr[i + 1]) or \
                (i % 2 == 0 and i + 1 < len( arr ) and arr[i] < arr[i + 1]):
                odd_c += 1
                max_val = max(max_val, odd_c)
            else:
                odd_c = 0
            
            # even turbulent
            if (i % 2 == 0 and i + 1 < len( arr ) and arr[i] > arr[i + 1]) or \
                (i % 2 == 1 and i + 1 < len( arr ) and arr[i] < arr[i + 1]):
                even_c += 1
                max_val = max(max_val, even_c)
            else:
                even_c = 0
        
        return max_val + 1
        