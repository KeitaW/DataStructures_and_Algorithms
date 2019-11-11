from binary_search.Find_Minimum_in_Ratoted_Sorted_Array.main import Solution


def test_main():
    solution = Solution()
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([1, 2]) == 1
    assert solution.findMin([2, 3, 4, 5, 1]) == 1
