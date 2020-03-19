from hashtable.IsmorphicStrings.main import Solution


def test_main():
    solution = Solution()
    # assert solution.isIsomorphic("egg", "add")
    # assert not solution.isIsomorphic("foo", "bar")
    # assert solution.isIsomorphic("paper", "title")
    assert not solution.isIsomorphic("ab", "aa")
