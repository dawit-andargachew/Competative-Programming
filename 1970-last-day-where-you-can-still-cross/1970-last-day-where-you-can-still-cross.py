class Solution:
    def latestDayToCross(self, row_count: int, column_count: int, cells: List[List[int]]) -> int:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        water = {}

        def find(location) -> (int, int):
            parent_location = water[location][0]
            if parent_location == location:
                return location
            water[location][0] = find(parent_location)
            return water[location][0]

        def union(location1, location2):
            rep1 = find(location1)
            rep2 = find(location2)
            if rep1 == rep2:
                return
            water[rep2][0] = location1
            _, left_connected_rep2, right_connected_rep2 = water[rep2]
            water[rep1][1] = water[rep1][1] or left_connected_rep2
            water[rep1][2] = water[rep1][2] or right_connected_rep2

        for previous_day, (row, column) in enumerate(cells):
            location = (row, column)
            # 1 indexed 
            left_connected = column == 1
            right_connected = column == column_count
            water[location] = [location, left_connected, right_connected]
            for r, c in directions:
                adjacent_spot = (row + r, column + c)
                if adjacent_spot not in water:
                    continue
                union(location, adjacent_spot)
            rep = find(location)
            _, left_connected, right_connected = water[rep]
            if left_connected and right_connected:
                return previous_day
        return -1