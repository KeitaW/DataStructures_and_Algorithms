from recursion.Pascals_Triangle.main import Solution


def test_main():
    solution = Solution()
    assert solution.generate(3) == [1, 3, 3, 1]
