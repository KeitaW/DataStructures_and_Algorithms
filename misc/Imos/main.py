
import numpy as np
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


"""問題
あなたは様々な種類のモンスターを捕まえるゲームをしています．今あなたがいるのは W×H のタイルからなる草むらです．この草むらでは N 種類のモンスターが現れます．モンスター i は Ai≦x<Bi, Ci≦y<Di の範囲にしか現れません．このゲームを効率的に進めるため，1 つのタイル上で現れるモンスターの種類の最大値が知りたいです．（ただし，W×H は計算可能な程度の大きさとし，N は大きくなりうるものとします．
https://imoz.jp/algorithms/imos_method.html
H: フィールド縦幅
W: フィールド横幅
N: モンスター数
A[i]: モンスターiの行動範囲横幅下限
B[i]: モンスターiの行動範囲横幅上限
C[i]: モンスターiの行動範囲縦幅下限
D[i]: モンスターiの行動範囲縦幅上限
"""


class Imos2d:
    def __init__(self) -> None:
        pass

    def solution_naive(self, H: int, W: int, N: int, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """O(NHW)
        """
        T = [[0 for _ in range(W)] for _ in range(H)]
        for i in range(N):
            for row in range(C[i], D[i]+1):
                for col in range(A[i], B[i]+1):
                    T[row][col] += 1
        return max([max(row) for row in T])

    def solution(self, H: int, W: int, N: int, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """O(N + HW)
        """
        T = [[0 for _ in range(W+1)] for _ in range(H+1)]
        for i in range(N):
            T[C[i]][A[i]] += 1  # 左上
            T[C[i]][B[i]+1] -= 1  # 右上
            T[D[i]+1][B[i]+1] += 1  # 右下
            T[D[i]+1][A[i]] -= 1  # 左下
        # 横方向の累積和
        print("")
        print(np.array(T))
        for row in range(H):
            for col in range(1, W):
                T[row][col] += T[row][col-1]
        for row in range(1, H):
            for col in range(W):
                T[row][col] += T[row-1][col]
        print(T)
        return max([max(row) for row in T])
