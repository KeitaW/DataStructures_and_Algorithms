from array_and_string.Remove_Element.main import Solution


def test_main():
    solution = Solution()
    assert solution.removeElement([3, 2, 2, 3], 3) == 2
    assert solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
