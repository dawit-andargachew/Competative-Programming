class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        map = defaultdict(int)
        low, i,max_length= 0, 0, 0

        # to track the number of swaps needed, use a dict and store each letter frequency
        # We can only make k swaps
        #                     so, sum of all elements other than the letter with max frequency should be <= k
        #                      Meaning, element max frequency doesn't need a swap, but to maximize the length other letters should be swaped
        while i < len(s):

            map[s[i]] += 1

            # sum of all elements occurence other than the max element
            sum_without_max = sum(map.values()) - max( map.values())

            if sum_without_max > k:
                
                while low < len(s) and sum_without_max > k:
                    map[s[low]] -= 1

                    if map[ s[low] ] == 0:
                        map.pop( s[low])

                    low += 1
                    # recalculate the sum_without_max
                    sum_without_max = sum(map.values()) - max( map.values())
            
            max_length = max(max_length, i - low + 1)

            i += 1

        return max_length