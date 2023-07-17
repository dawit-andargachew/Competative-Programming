from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        mod = 10**9 + 7
        s = SortedList()
        answer = 0
        
        # bisect_left and bisect_right return the leftmost and rightmost
        # index where the value can be inserted without
        # changing the order of elements. If the value does not exist in the list, 
        # they both return the same index. 
        # The difference arises when the value exists in the list. 
    
        for i in instructions:
            numberOfLess = s.bisect_left(i)
            numberOfGreater =  len(s) - s.bisect_right(i)
            
            answer += min(numberOfLess, numberOfGreater)
            s.add(i)
        
        return answer % mod