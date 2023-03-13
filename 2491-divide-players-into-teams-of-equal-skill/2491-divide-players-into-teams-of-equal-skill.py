class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        # sort to group players
        skill.sort()
        l,r = 0, len(skill) - 1
        
        # sum of player
        player_sum = skill[l] + skill[r]
        
        # sum of total_chemistry of all groups
        total_chemistry = skill[l] * skill[r]
        l += 1
        r -= 1
        
        while l < r:
            temp_sum = skill[l] + skill[r]
            if temp_sum == player_sum:
                total_chemistry += skill[l] * skill[r]
            else:
                total_chemistry = -1
                break
            
            l += 1
            r -= 1          
        
        return total_chemistry