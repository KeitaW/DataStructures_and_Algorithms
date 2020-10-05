from binary_search.Find_Minimum_in_Ratoted_Sorted_ArrayII.main import Solution


def test_main():
    solution = Solution()
    # assert solution.findMin([3, 4, 5, 1, 2]) == 1
    # assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    # assert solution.findMin([1, 2]) == 1
    assert solution.findMin([2, 3, 4, 5, 1]) == 1
    assert solution.findMin([2, 2, 2, 0, 1]) == 0
    assert solution.findMin([3, 1, 3]) == 1
    assert solution.findMin([1, 3, 5]) == 1


if __name__ == "__main__":
    test_main()
