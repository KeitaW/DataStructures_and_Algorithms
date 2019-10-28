from array_and_string.strStr.main import Solution


def test_main():
    solution = Solution()
    solution.strStr("hello", "ll") == 2
    solution.strStr("a", "a") == 0
    solution.strStr("mississippi", "pi") == 9
