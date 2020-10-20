from hashtable.ContainsDuplicateII.main import Solution


def test_main():
    solution = Solution()
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
