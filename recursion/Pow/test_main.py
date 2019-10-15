import pytest

from recursion.Pow.main import Solution


def test_pow():
    solution = Solution()
    assert solution.myPow(2.0, 10) == pytest.approx(1024.0)
    assert solution.myPow(2.1, 3) == pytest.approx(9.26100)
    assert solution.myPow(2.0, -2) == pytest.approx(0.25)
