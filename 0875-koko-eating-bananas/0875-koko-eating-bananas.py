class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            k = piles[0]// h
            k += 1 if piles[0] % h != 0 else 0
            return k


        low  = 1 # make it is one, why One? 
        high = sum(piles)
        k = 0

        while low <= high:
            mid = low + (high - low)//2
            
            count = 0
            for i in piles:
                if i <= mid:
                    count += 1
                else:
                    count += i//mid 
                    count += 1 if i % mid != 0 else 0

            # print(count, low, high)
            if count <= h:
                # if count == h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1


        return k