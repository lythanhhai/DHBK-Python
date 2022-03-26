from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        perimeter = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += 4
                    if(row > 0 and grid[row - 1][col] == 1):
                        perimeter -= 2
                    if(col > 0 and grid[row][col - 1] == 1):
                        perimeter -= 2
        return perimeter