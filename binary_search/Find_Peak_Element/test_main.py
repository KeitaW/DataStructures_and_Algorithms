from binary_search.Find_Peak_Element.main import Solution


def test_main():
    solution = Solution()
    assert solution.findPeakElement([1, 2, 3, 1]) == 2
    assert solution.findPeakElement(
        [1, 2, 1, 3, 5, 6, 4]) == 1 or solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
    assert solution.findPeakElement([1, 2]) == 1
