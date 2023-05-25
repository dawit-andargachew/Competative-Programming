class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        
        # make sure the first value is 1
        arr[0] = 1

        # after each consecutive value make sure difference is not more than one
        for i in range(1, len(arr) ):

            # difference > 1, so decrease the value and make the difference 1
            # making the difference one helps to get maximum possible value
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1]+1
        
        return arr[-1]