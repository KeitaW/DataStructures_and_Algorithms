from array_and_string.Rotate_Array.main import Solution


def test_main():
    solution = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(id(arr))
    solution.rotate(arr, 3)
    assert arr == [5, 6, 7, 1, 2, 3, 4]
    arr = [1, 2]
    solution.rotate(arr, 1)
    assert arr == [2, 1]
    arr = [1, 2]
    solution.rotate(arr, 2)
    assert arr == [1, 2]
