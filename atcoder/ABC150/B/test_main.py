from atcoder.ABC150.B.main import Solution


def test_main():
    solution = Solution()
    assert solution.CountABC("ZABCDBABCQ") == 2
    assert solution.CountABC("ZABCDBABCQABC") == 3
    assert solution.CountABC("ABC") == 1
