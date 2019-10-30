from array_and_string.Max_Consecutive_Ones.main import Solution


def test_main():
    solution = Solution()
    assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
