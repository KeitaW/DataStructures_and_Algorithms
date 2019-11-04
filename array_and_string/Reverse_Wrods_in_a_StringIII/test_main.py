from array_and_string.Reverse_Wrods_in_a_String.main import Solution


def test_main():
    solution = Solution()
    assert solution.reverseWords(
        "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
