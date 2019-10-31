from array_and_string.Minimum_Size_Subarray_Sum.main import Solution


def test_main():
    solution = Solution()
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5
