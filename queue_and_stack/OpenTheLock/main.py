from typing import List, Generator
from queue import Queue

NDIGITS = 4


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """You have a lock in front of you with 4 circular wheels.
        Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
        The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
        Each move consists of turning one wheel one slot.
        The lock initially starts at '0000', a string representing the state of the 4 wheels.
        You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
        the wheels of the lock will stop turning and you will be unable to open it.
        Given a target representing the value of the wheels that will unlock the lock,
        return the minimum total number of turns required to open the lock, or -1 if it is impossible.
        
        Parameters
        ----------
        deadends : List[str]
        target : str
        
        Returns
        -------
        int
        """

        def neighbors(digits: str) -> Generator[str, None, None]:
            for i in range(NDIGITS):
                digit = int(digits[i])
                for diff in [1, -1]:
                    next_digit = (digit + diff) % 10
                    yield digits[:i] + str(next_digit) + digits[i + 1 :]

        deadends = set(deadends)
        digits = "0000"
        visited = {digits}
        queue = Queue()
        queue.put((digits, 0))  # The second element represents number of operations.
        while not queue.empty():
            digits, n_operations = queue.get()
            if digits == target:
                return n_operations
            if digits in deadends:
                continue
            for next_digits in neighbors(digits):
                if next_digits not in visited:
                    visited.add(next_digits)
                    queue.put((next_digits, n_operations + 1))
        return -1

