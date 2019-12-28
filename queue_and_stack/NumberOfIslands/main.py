from typing import List
from queue import Queue
from itertools import product

LAND = "1"
WATER = "0"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        nrow, ncol = len(grid), len(grid[0])
        num_islands = 0
        neighbors = Queue()
        for r, c in product(range(nrow), range(ncol)):
            if grid[r][c] == LAND:
                num_islands += 1
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
                if col + 1 <= ncol - 1 and grid[row][col + 1] == LAND:
                    neighbors.put((row, col + 1))
        return num_islands

