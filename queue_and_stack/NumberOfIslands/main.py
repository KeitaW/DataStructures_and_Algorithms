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
        for row, col in product(range(nrow), range(ncol)):
            if grid[row][col] == LAND:
                pass

