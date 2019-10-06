from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def init(row, triangle=[]):
            return init(row-1, [[1]*row] + triangle) if row > 0 else triangle
        triangle = init(numRows)

        for i in range(numRows):
            for j in range(i):
                triangle[i][j] = 1 if (j == 0 or i == j) \
                    else triangle[i-1][j-1] + triangle[i-1][j]
        return triangle
