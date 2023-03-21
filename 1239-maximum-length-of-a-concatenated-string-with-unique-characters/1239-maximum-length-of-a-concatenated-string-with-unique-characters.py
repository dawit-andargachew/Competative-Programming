class Solution:
    def maxLength(self, arr: List[str]) -> int:

        acc = []
        max_length = 0
        def backtrack( idx, a):
            nonlocal max_length

            for i in range(idx, len(arr)):
                
                # if the the given string has
                # either repeated characters in it 
                # or it has common characters with its previous character
                # so skipt it
                if len( set( arr[i] ) ) != len( arr[i] )  or a and len( a.intersection( set(arr[i])) ) > 0:
                    continue
                
                a = a.union( set( arr[i] ) ) # track unique charcters in a set
                max_length = max( max_length, len( a )) # udpate maximum length
                
                # PICK OPTION
                acc.append( arr[i] )
                backtrack( i + 1, a)

                # DON'T PICK OPTION
                a.symmetric_difference_update( set( acc[-1]) ) # remove elements from the given set
                acc.pop()
            
        backtrack(0, set())

        return max_length