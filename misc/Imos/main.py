
from typing import List

"""問題
あなたは喫茶店を経営しています．あなたの喫茶店を訪れたそれぞれのお客さん i (0≤i<C) について入店時刻 Si と出店時刻 Ei が与えられます（0≤Si<Ei≤T）．
同時刻にお店にいた客の数の最大値 M はいくつでしょうか．ただし，同時刻に出店と入店がある場合は出店が先に行われるものとします．
（また解法としては，C が非常に大きい場合でも O(C+T) の計算量で解けることが期待されているものとします．）
https://imoz.jp/algorithms/imos_method.html
C: 顧客数
T: 時間窓
S[i]: 顧客iの入店時間
E[i]:  顧客iの退店時間
"""


class Imos1d:
    def __init__(self) -> None:
        pass

    def solution_naive(self, T: int, C: int, S: List[int], E: List[int]) -> int:
        """ O(CT)
        """
        table = [0] * T
        for i in range(C):
            for j in range(S[i], E[i]):
                table[j] += 1
        return max(table)

    def solution(self, T: int, C: int, S: List[int], E: List[int]) -> int:
        """ O(C + T)
        """
        table = [0] * T
        for i in range(C):
            table[S[i]] += 1
            table[E[i] - 1] -= 1
        for i in range(1, T):
            table[i] += table[i-1]
        return max(table)


class Imos2d:
    def __init__(self) -> None:
        pass

    def solution_naive(self, T: int, C: int, S: List[int], E: List[int]) -> int:
        pass

    def solution(self, T: int, C: int, S: List[int], E: List[int]) -> int:
        pass
