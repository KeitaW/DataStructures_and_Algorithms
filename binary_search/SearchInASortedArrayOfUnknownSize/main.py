# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

MAX_LENGTH = 10 ** 4
OUT_OF_BOUNDS = 2147483647


def binary_search_meguru(f: Callable[[int], bool], ok: int, ng: int) -> int:
    """General purpose binary search algorithm
    Parameters
    ----------
    f : Callable[[int], int]
        Monotonically increasing function
    left : int
        The left initial value that satisfies f(x) == True
    right : int
        The right initial value that satisfies f(x) == False
    Returns
    -------
    int
        The minimum x that satisfies f(x) = True
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        def is_range(idx: int) -> bool:
            return reader.get(idx) < OUT_OF_BOUNDS

        array_length = binary_search_meguru(is_range, 0, MAX_LENGTH)

        ng, ok = -1, array_length
        lower_bound = binary_search_meguru(
            lambda idx: reader.get(idx) >= target, ok, ng
        )
        if reader.get(lower_bound) == target:
            return lower_bound
        else:
            return -1

