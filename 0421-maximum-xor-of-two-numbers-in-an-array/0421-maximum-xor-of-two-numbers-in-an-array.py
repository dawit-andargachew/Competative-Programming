class Trie:
    def __init__(self):
        self.root = {}
        self.m = 0
    
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]
        
    def compare(self,word,i):
        node=self.root
        t=""
        a,b='0','1'
        for ch in word:
            if ch==a and b in node:
                t+=b
                node=node[b]
            elif ch==b and a in node:
                t+=a
                node=node[a]
            else:
                t+=ch
                node=node[ch]
        self.m=max(self.m,int(t,2)^i)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Trie()
        for i in nums:
            word="{:032b}".format(i)
            trie.insert(word)
        for i in nums:
            word="{:032b}".format(i)
            trie.compare(word,i)
        return trie.m