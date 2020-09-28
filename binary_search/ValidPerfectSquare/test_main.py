from binary_search.ValidPerfectSquare.main import Solution


def test_main():
    solution = Solution()
    assert solution.isPerfectSquare(4) is True
    assert solution.isPerfectSquare(5) is False

