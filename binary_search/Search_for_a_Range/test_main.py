from binary_search.Search_for_a_Range.main import Solution


def test_main():
    solution = Solution()
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solution.searchRange([1, 1, 1], 1) == [0, 2]
    assert solution.searchRange([0, 1, 2, 3, 4, 4, 4], 2) == [2, 2]
