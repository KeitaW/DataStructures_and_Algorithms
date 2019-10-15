class Solution:
    def myPow(self, x: float, n: int, accumulator: float = 1.0) -> float:
        """Pow by fast power algorithm

        Parameters
        ----------
        x : float
            x raised to 
        n : int
            the power n

        Returns
        -------
        float
            x ** n
        """
        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n//2)
            return half * half if n % 2 == 0 else half * half * x
        if n < 0:
            x = 1 / x
            n = -n
        return fastPow(x, n)

    def myPow_tail_recursion(self, x: float, n: int, accumulator: float = 1.0) -> float:
        """Pow by tail recursion 

        Parameters
        ----------
        x : float
            x raised to 
        n : int
            the power n

        Returns
        -------
        float
            x ** n
        """
        return self.myPow(x, n-1, accumulator * x) if n >= 1 else (
            self.myPow(x, n+1, accumulator / x) if n <= -1 else (
                accumulator
            )
        )
