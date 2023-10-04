class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(list(zip(ages, scores)), reverse = True)
        dp = [0] * len(scores)
        ans = 0
        
        for i in range(len(scores)):
            dp[i] = players[i][1]
            score = dp[i]
            
            for j in range(i):
                if players[i][0] == players[j][0] or players[i][1] <= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
                    
                score = max(score, dp[i])
                
            ans = max(ans, score)
            
        return ans