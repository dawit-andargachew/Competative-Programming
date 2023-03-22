class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        merge = ""
        
        # select element from lexicographically greater part and reassign it again
        while word1 or word2:
            if word1 >= word2:
                merge += word1[0]
                word1 = word1[1:]
            else:
                merge += word2[0]
                word2 = word2[1:]
        
        return merge
        