class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # https://www.youtube.com/watch?v=jFeCO8Gxc3k

        # assume each character reprsents a bit
        # like a = 1, b = 10, c = 100..., each letter represents shifting 1 to the left with ord(char) - 97 times
        bits = []
        for word in words:

            # for each words store each on bit by using or like this
            # "abcw" = 1 | 10 | 100 | 100000000000000...
            to_int = 0
            for w in word:
                a = ord(w)- 97
                a = 1 << a
                to_int |= a
            bits.append(to_int)

        max_length, size = 0, len(words)
        for i in range(size):
            for j in range(i + 1, size):
                result = bits[i] & bits[j]

                # if two string have common charater like "abc" = 111, "ead" = 11001
                # "abc" & "ead" = non-zero because they will have at least one common bit
                if result == 0:
                    max_length = max( max_length, len(words[i]) * len(words[j]))

        return max_length