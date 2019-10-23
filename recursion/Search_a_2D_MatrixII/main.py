from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        The matrix has the following property.
            * Integers in each row are sorted in ascending from left to right.
            * Integers in each column are sorted in ascending from top to bottom.
        """
        if not matrix:
            return False

        def check_row(idx: int) -> bool:
            """
            Time Complexity: O(N+M)
            Space Complexity: 1
            """
            if idx == len(matrix):
                return False
            if (matrix[idx][0] <= target <= matrix[idx][-1] and target in matrix[idx]):
                return True
            return check_row(idx+1)
        return check_row(0) if matrix and matrix[0] else False
