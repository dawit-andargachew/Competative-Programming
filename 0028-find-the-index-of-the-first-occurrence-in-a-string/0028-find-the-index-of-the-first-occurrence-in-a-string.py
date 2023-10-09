class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # make string match starting from each possible options
        for i in range( len(haystack) ):
            if haystack[i] == needle[0]: # the starting symbol is the same so continue matching
                index, temp = i, 0
                while index < len(haystack) and temp < len(needle):
                    if haystack[index] == needle[temp]:
                        temp += 1
                    else:
                        break
                    index += 1

                # we get a possible match, so return index
                if temp == len(needle):
                    return index - temp


        return -1
        