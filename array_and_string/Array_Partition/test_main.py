from array_and_string.Array_Partition.main import Solution


def test_main():
    solution = Solution()
    assert solution.arrayPairSum([1, 4, 3, 2]) == 4
    assert solution.arrayPairSum([1, 1]) == 1
