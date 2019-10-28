from array_and_string.Longest_Common_Prefix.main import Solution


def test_main():
    solution = Solution()
    solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    solution.longestCommonPrefix(["dog", "racecar", "car"]) == "fl"
