from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

        Parameters
        ----------
        numRows : int
            The row index

        Returns
        -------
        List[List[int]]
            The numRows th index row of the Pascal's triangle

        Notes
        ------
        You can only use O(k) extra space.
        """
        def init(row, triangle=[]):
            return init(row-1, [[1]*row] + triangle) if row > 0 else triangle
        triangle = init(numRows)

        for i in range(numRows):
            for j in range(i):
                triangle[i][j] = 1 if (j == 0 or i == j) \
                    else triangle[i-1][j-1] + triangle[i-1][j]
        return triangle
