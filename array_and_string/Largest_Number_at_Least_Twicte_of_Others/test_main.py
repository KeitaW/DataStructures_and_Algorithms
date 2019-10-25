from array_and_string.Largest_Number_at_Least_Twicte_of_Others.main import Solution


def test_main():
    solution = Solution()
    assert solution.dominantIndex([3, 6, 1, 0]) == 1
    assert solution.dominantIndex([1, 2, 3, 4]) == -1
