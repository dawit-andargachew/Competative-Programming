class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = 0
        low = max(weights)
        high = sum(weights)


        while low <= high:
            mid = low + (high - low)//2 

            count = 0
            widhgt_sum = 0
            for i in weights:
                widhgt_sum +=i
                if widhgt_sum > mid:
                    count += 1
                    widhgt_sum = i
            count += 1

            # print(mid, low, high)
            if count <= days:
                min_weight = mid
                high = mid - 1
            else:
                low = mid + 1        

        return min_weight