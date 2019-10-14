class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N not in self.cache:
            self.cache[N] = self.fib(N-1) + self.fib(N-2)
        return self.cache[N]
