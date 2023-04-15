class ThroneInheritance:

    # This question asks just to implement graph for throne inheritance and 
    # when we generate inheritance order just exclude deaths
    def __init__(self, kingName: str):
        self.kingName = kingName
        self.throne = defaultdict(list)
        self.deaths = set()
        
    # when a child is born, add to the parent's list
    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append(childName)        

    # when death happens, store in a set
    def death(self, name: str) -> None:
        self.deaths.add(name)

    # to get inheritance order, we need two things
    # 1, king name => store the king name and traverse starting from the king
    # 2, death list => exlude deaths in the inheritace order
    def getInheritanceOrder(self) -> List[str]:

        answer, visited = [], set()
        def dfs(name):
            
            # exlude deaths in the inheritace
            if name not in self.deaths:
                answer.append(name)

            visited.add(name)
            for child in self.throne[name]:
                if child not in visited:
                    dfs(child)
        
        # start the dfs from the king
        dfs(self.kingName)
        return answer

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()