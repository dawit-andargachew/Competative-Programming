class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        temp = []
        for i in range(len(plantTime)):
            temp.append((growTime[i],i))
        
        temp.sort(reverse = True)
        ans = plantTime[0]
        curr = 0
        for i in range(len(temp)):
            ans = max(ans, curr + temp[i][0]+plantTime[temp[i][1]])
            curr = curr+plantTime[temp[i][1]]
        return ans