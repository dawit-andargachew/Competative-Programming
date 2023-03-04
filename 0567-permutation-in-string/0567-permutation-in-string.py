class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # it can be more efficent by applying map efficinetly,
        # and the solution is check for every substring of lenggh s1 on s2
        
        isPermutate = False
        dict_1 = Counter(s1)

        low = 0
        high = len(s1)
        while high <= len(s2):# sub-string is used so, <= have no problem
            
            # check for each substrin of length len(s1) on s2
            # and compare there map
            temp_dic = Counter( s2[low:high])
            if temp_dic == dict_1:
                isPermutate = True
                break
            else:
                low += 1
                high += 1

        return isPermutate