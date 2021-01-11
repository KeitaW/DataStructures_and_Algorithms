from typing import List
from itertools import accumulate


class CumSum:
    def __init__(self, vector: List[int]) -> None:
        self._cumsum = [0] + list(accumulate(vector))

    def cumsum(self, right: int, left: int):
        return self._cumsum[left] - self._cumsum[right]
