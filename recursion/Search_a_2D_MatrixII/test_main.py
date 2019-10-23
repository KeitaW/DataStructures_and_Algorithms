from recursion.Search_a_2D_MatrixII.main import Solution


def test_main():
    solution = Solution()
    assert solution.searchMatrix(
        [[-5]], -5
    ) == True

    assert solution.searchMatrix(
        [[]], 1
    ) == False

    assert solution.searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5
    ) == True
