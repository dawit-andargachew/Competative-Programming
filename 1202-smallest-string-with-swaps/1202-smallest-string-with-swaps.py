# Union Find implementation with classes
class DisJointSet:
    def __init__(self):
        self.representative = {}

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        self.representative[y_rep] = x_rep

    def find(self, x):
        if x not in self.representative:
            self.representative[x] = x
            return x

        val = x
        while x != self.representative[x]:
            x = self.representative[x]
        
        # path compression
        while val != self.representative[val]:
            parent = self.representative[val]
            self.representative[val] = x
            val = parent
            
        return x

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        # Lets group indices on the same group with Union and Find algorithm
        # then put the strings in one group in a single list and sort it

        dis  = DisJointSet()

        # group indices together with Union and Find
        for x, y in pairs:
            dis.union(x, y)

        # put characters in one group in to a single list
        collect = defaultdict(list)
        for i in range(len(s)):
            collect[ dis.find(i) ].append(s[i])

        # sort each list found on the same group
        # to access each char by index add index at the end of each list
        for k in collect:
            collect[k] = sorted(collect[k])
            collect[k].append(0) # add indexing option at the end
        
        # extract string starting from index 0 in each group
        # But, whenever a given group char is accessed, we need to increase indexing option by one
        # example, take testCase 1
        #   So we have two groups and 0 and 1 are as a representative
        #     {0: [b, d, 0], 1: [a, c, 0]}
        #   after accesssing index 0 on the map,  increase the indexing option on 0 by 1 
        #    then it becomes
        #    {0: [b, d, 1],  1: [a, c, 0]} => so next `d` will be accessed

        answer = []
        for i in range( len(s) ):
            represent = dis.find(i)
            char = collect[ represent ][collect[ represent ][-1]] # access the charter by the index found on the indexing option
            
            # append to th answer
            answer.append(char)

            # increase the indexing option by 1, so next time we index we will get the correct character
            collect[ represent ][-1] = collect[ represent ][-1] + 1
        
        # return the answer in string format
        return ''.join(answer)