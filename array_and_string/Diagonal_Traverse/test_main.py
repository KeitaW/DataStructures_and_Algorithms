from array_and_string.Diagonal_Traverse.main import Solution


def test_main():
    solution = Solution()
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution.findDiagonalOrder(arr) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    assert solution.findDiagonalOrder(
        arr) == [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
