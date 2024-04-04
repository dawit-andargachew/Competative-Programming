class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        # forbidden is 10 chars long max, so bruteforce is also possible
        left = answer = 0
        store = set(forbidden)
        for i in range( len(word) ):
            for j in range( max(left, i - 9), i + 1):
                if word[j:i+1] in store:
                    left = j + 1
            answer = max(answer, i - left + 1)

        return answer
        