from array_and_string.Move_Zeros.main import Solution


def test_main():
    solution = Solution()
    arr = [0, 1, 0, 3, 12]
    solution.moveZeroes(arr)
    assert arr == [1, 3, 12, 0, 0]
    arr = [0, 0, 1]
    solution.moveZeroes(arr)
    assert arr == [1, 0, 0]
