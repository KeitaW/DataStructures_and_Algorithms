from misc.Imos.main import Imos1d


def test_Imos1d():
    T = 10
    C = 2
    S = [0, 5]
    E = [9, 10]
    imos1d = Imos1d()
    assert imos1d.solution_naive(T, C, S, E) == 2
    assert imos1d.solution(T, C, S, E) == 2
