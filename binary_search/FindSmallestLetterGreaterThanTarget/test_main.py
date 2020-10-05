from binary_search.FindSmallestLetterGreaterThanTarget.main import Solution


def test_main():
    solution = Solution()
    assert solution.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert solution.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert solution.nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert solution.nextGreatestLetter(["c", "f", "j"], "g") == "j"
    assert solution.nextGreatestLetter(["c", "f", "j"], "k") == "c"
    assert solution.nextGreatestLetter(["a", "b"], "z") == "a"
