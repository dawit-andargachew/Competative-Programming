class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        # 2 pointer approach, it can also be binary search

        a, b, store = 0, 0, -1
        while a < len(houses) and b < len(heaters):

            curr = abs(houses[a] - heaters[b])
            temp = b
            while temp < len(heaters) and curr >= abs(houses[a] - heaters[temp]):
                curr = min(curr, abs(houses[a] - heaters[temp]))
                temp += 1

            # after checking forwared on heaters, move one possition backward
            # am checking the smallest so, the smalles is found on temp - 1
            # take houses = [5, 6, 20 , 30 , 40] and  heaters = [1, 10, 11, 12]
            # for abs(5-1) => 4
            # for abs(5-10) => 5
            # 5 is larger than 4, so when we check for 6 we should start from 4, 
            # that is why we need b = temp - 1
            b = temp - 1
            store = max(curr, store)
            a += 1

        # handle edge cases when the last home is very far from the furthest heater
        # like 
        #    houses = [5, 6, 20 , 30 , 40]
        #    heaters = [1, 10, 11, 12]
        #so 40 - 12 = 28,
        # store = max(store, 28) is the minimum radius we need to make all houses warm
        if a < len(houses) and b == len(heaters):
            ans = houses[-1] - heaters[-1]
            store = max(ans, store)

        return store