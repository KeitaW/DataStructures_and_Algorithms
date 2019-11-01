from array_and_string.Spiral_Matrix.main import Solution


def test_main():
    solution = Solution()
    print(solution.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    assert solution.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
