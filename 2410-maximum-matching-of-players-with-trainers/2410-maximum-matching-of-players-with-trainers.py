class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        # sort these arrays before find mathcing
        players.sort()
        trainers.sort()
        
        matching = 0
        i, j = 0, 0
        
        # whenever we get a match, update matching and increase players pointer
        while i < len( players ) and j < len( trainers ):

            if players[i] <= trainers[j]:
                i += 1
                matching += 1
            
            j += 1

        return matching