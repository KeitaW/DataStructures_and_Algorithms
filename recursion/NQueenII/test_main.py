from recursion.NQueenII.main import Solution


def test_main():
    solution = Solution()
    assert solution.totalNQueens(n=4) == 2
