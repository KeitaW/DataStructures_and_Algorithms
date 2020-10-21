from hashtable.ContainsDuplicateII.main import Solution


def test_main():
    solution = Solution()
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
