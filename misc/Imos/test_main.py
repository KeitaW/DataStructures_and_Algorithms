from misc.Imos.main import Imos1d, Imos2d


def test_Imos1d():
    T = 10
    C = 2
    S = [0, 5]
    E = [9, 10]
    imos1d = Imos1d()
    assert imos1d.solution_naive(T, C, S, E) == 2
    assert imos1d.solution(T, C, S, E) == 2


def test_Imos2d():
    H = 6
    W = 6
    N = 3
    A = [0, 1, 2]
    B = [3, 2, 5]
    C = [0, 3, 2]
    D = [3, 4, 5]
    imos2d = Imos2d()
    assert imos2d.solution_naive(H, W, N, A, B, C, D) == 3
