from recursion.Climbing_Stairs.main import Solution


def test_main():
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(4) == 5
