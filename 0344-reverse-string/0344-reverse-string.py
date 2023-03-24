class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse_func(left,right):
            if left >= right:
                return
            # make a swap to reverse strings
            s[left], s[right] = s[right], s[left]
            
            reverse_func(left + 1, right - 1)

        reverse_func(0, len(s)-1)