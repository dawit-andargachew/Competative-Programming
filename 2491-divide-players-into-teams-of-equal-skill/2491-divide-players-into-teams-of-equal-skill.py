class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        l,r = 0, len(skill) - 1
        
        player = skill[l] + skill[r]
        total = skill[l] * skill[r]
        l += 1
        r -= 1
        while l < r:
            temp = skill[l] + skill[r]
            if temp == player:
                total += skill[l] * skill[r]
            else:
                total = -1
                break
            
            l += 1
            r -= 1          
        
        return total