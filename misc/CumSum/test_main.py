from misc.CumSum.main import CumSum


def test_cumsum():
    cumsum = CumSum([1, 2, 3])
    assert cumsum.cumsum(1, 3) == 5
    cumsum = CumSum([1, 2, 3, 5, 5, 5, -1, -1, -1])
    assert cumsum.cumsum(3, 6) == 15
