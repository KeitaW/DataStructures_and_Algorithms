from array_and_string.Remove_Duplicates_from_Sorted_Array.main import Solution


def test_main():
    solution = Solution()
    arr = [1, 1, 2]
    assert solution.removeDuplicates(arr) == 2
    assert arr == [1, 2]
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert solution.removeDuplicates(arr) == 5
    assert arr == [0, 1, 2, 3, 4]
    arr = [1]
    assert solution.removeDuplicates(arr) == 1
    assert arr == [1]
    arr = [1, 1, 1]
    assert solution.removeDuplicates(arr) == 1
    assert arr == [1]
