from hashtable.IntersectionofTwoArrarysII.main import Solution


def test_main():
    solution = Solution()
    assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
