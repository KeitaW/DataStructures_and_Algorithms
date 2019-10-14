from typing import List
from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

        Parameters
        ----------
        numRows : int
            The row index

        Returns
        -------
        List[int]
            The numRows th index row of the Pascal's triangle

        Notes
        ------
        You can only use O(k) extra space.
        """

        def n_combinations(n, m):
            return int(factorial(n) / (factorial(m) * factorial(n-m)))
        n = rowIndex
        rows = [n_combinations(n, m-1) for m in range(1, n+2)]
        return rows
