from array_and_string.Add_Binary.main import Solution


def test_main():
    solution = Solution()
    a = "11"
    b = "1"
    assert solution.addBinary(a, b) == "100"
