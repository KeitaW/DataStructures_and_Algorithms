from array_and_string.Reverse_Wrods_in_a_String.main import Solution


def test_main():
    solution = Solution()
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
