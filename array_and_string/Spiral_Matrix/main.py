from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral_coords(bottom, top, left, right):
            for col in range(left, right + 1):
                # Right
                yield bottom, col
            for row in range(bottom + 1, top + 1):
                # Down
                yield row, right
            if bottom < top and left < right:
                for col in range(right - 1, left - 1, -1):
                    # Left
                    yield top, col
                for row in range(top - 1, bottom, -1):
                    # Up
                    yield row, left

        if not matrix:
            return []
        output = []
        bottom, top = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while bottom <= top and left <= right:
            print(bottom, top, left, right)
            output += [
                matrix[r][c]
                for r, c in spiral_coords(bottom, top, left, right)
            ]
            bottom += 1
            top -= 1
            left += 1
            right -= 1
        return output
