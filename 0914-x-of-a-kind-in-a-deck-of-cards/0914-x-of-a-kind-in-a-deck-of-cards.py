class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return
        
        # helps to find the GCF
        def GCF(a, b):
            if b == 0:
                return a
            return GCF(b, a % b)
        
        
        freq = Counter(deck)

        # the gcf of all frequencies should be more than 1
        # So calculate gcf and check gcf == 1 or not
        gcf = freq[ deck[0] ]
        for key in freq:
            gcf = GCF(gcf,freq[key])

        # check gcf equal to 1
        return gcf != 1