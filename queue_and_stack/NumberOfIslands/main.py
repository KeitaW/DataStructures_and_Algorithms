from typing import List
from queue import Queue
from itertools import product

LAND = "1"
WATER = "0"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.

        Input:
        11110
        11010
        11000
        00000

        Output: 1
        
        Parameters
        ----------
        grid : List[List[str]]
        
        Returns
        -------
        int
        """
        if len(grid) == 0:
            return 0
        nrow, ncol = len(grid), len(grid[0])
        num_islands = 0
        neighbors = Queue()
        for r, c in product(range(nrow), range(ncol)):
            if grid[r][c] == LAND:
                num_islands += 1
                grid[r][c] = WATER
                neighbors.put((r, c))
            while not neighbors.empty():
                row, col = neighbors.get()
                if row - 1 >= 0 and grid[row - 1][col] == LAND:
                    neighbors.put((row - 1, col))
                    grid[row - 1][col] = WATER
                if row + 1 <= nrow - 1 and grid[row + 1][col] == LAND:
                    neighbors.put((row + 1, col))
                    grid[row + 1][col] = WATER
                if col - 1 >= 0 and grid[row][col - 1] == LAND:
                    neighbors.put((row, col - 1))
                    grid[row][col - 1] = WATER
                if col + 1 <= ncol - 1 and grid[row][col + 1] == LAND:
                    neighbors.put((row, col + 1))
                    grid[row][col + 1] = WATER
        return num_islands

