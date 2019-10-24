class Solution:
    def totalNQueens(self, n: int) -> int:
        """Backtrack possible alignment of queens
        and returns the number of distinct solutions to the n-queens puzzle

        Parameters
        ----------
        n : int
            Number of Queens

        Returns
        -------
        int
            Number of distinct solutions
        """
        self.n = n
        self.rows = [True] * n
        self.dales = [True] * n
        return self.backtrack_nqueen()

    def is_not_under_attack(self, row, col):
        return rows[col] and hills[row - col] and dales[row + col]

    def place_queen(self, row, col):
        rows[col] = False
        hills[row - col] = False
        dales[row + col] = False

    def remove_queen(self, row, col):
        rows[col] = True
        hills[row - col] = True
        dales[row + col] = True

    def backtrack_nqueen(self, row=0, count=0):
        for col in range(n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                if row + 1 == n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                else:
                    # we move on to the next row
                    count = self.backtrack(row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)
        return count
