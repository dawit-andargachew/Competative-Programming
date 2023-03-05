class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        
        total_moves = 0
        
        for i in range( len(seats)):
            total_moves += abs( seats[i] - students[i])
        
        return total_moves
        