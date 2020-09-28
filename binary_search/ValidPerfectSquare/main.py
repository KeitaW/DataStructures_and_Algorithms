from typing import Callable


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
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        def condition(x):
            return x ** 2 <= num

        lower_bound = binary_search_meguru(condition, 2, num // 2 + 1)
        return True if lower_bound ** 2 == num else False

