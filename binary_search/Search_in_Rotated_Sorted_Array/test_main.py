from binary_search.Search_in_Rotated_Sorted_Array.main import find_rotation_index, Solution


def test_find_rotation_index():
    assert find_rotation_index([1]) == 0
    assert find_rotation_index([4, 5, 6, 1, 2, 3]) == 3
    assert find_rotation_index([3, 1, 2]) == 1


def test_main():
    solution = Solution()
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solution.search([4, 5, 1, 2, 3], 1) == 2
