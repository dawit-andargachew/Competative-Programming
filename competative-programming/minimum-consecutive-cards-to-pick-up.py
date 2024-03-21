class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        ans = 1_000_000
        table = defaultdict(int)
        for idx, value in enumerate( cards ):
            if value  in table:
                ans = min(ans, idx - table[value ] + 1)
            
            table[ value ] = idx
        
        return ans if ans != 1_000_000 else -1