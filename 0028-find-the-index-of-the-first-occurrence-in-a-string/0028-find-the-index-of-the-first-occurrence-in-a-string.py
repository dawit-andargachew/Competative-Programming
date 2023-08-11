class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        initialPoints = []
        # store possible start points
        for i in range( len(haystack) ):
            if haystack[i] == needle[0]:
                initialPoints.append(i)

        # make string match starting from each possible options
        for i in initialPoints:
            index, temp = i, 0
            while index < len(haystack) and temp < len(needle):
                if haystack[index] == needle[temp]:
                    temp += 1
                else:
                    break
                index += 1
            
            # we get a possible mathc, so return index
            if temp == len(needle):
                return index - temp


        return -1
        