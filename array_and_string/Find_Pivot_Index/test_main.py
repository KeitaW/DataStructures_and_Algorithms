from array_and_string.Find_Pivot_Index.main import Solution


def test_main():
    solution = Solution()
    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 3]) == -1
    assert solution.pivotIndex([-1, -1, -1, 0, 1, 1]) == 0
    assert solution.pivotIndex([-1, -1, 0, 1, 1, 0]) == 5
