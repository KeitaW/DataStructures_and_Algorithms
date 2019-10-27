from typing import List
from copy import copy
from itertools import chain


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        up = True
        x, y = 0, 0
        dim_y = len(matrix)
        dim_x = len(matrix[0]) if dim_y > 0 else 0
        if dim_y == 0:
            return []
        output = [None] * (dim_x * dim_y)
        for i in range(dim_x * dim_y):
            output[i] = matrix[y][x]
            if up:
                if x == dim_x - 1:
                    y = y + 1
                    up = False
                elif y == 0:
                    x = x + 1
                    up = False
                else:
                    x += 1
                    y -= 1
                    up = True
            else:
                if y == dim_y - 1:
                    x = x + 1
                    up = True
                elif x == 0:
                    y = y + 1
                    up = True
                else:
                    x -= 1
                    y += 1
        return output

    def _findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """正方行列ではWorkする...

        Parameters
        ----------
        matrix : List[List[int]]
            [description]

        Returns
        -------
        List[int]
            [description]
        """
        def gen_chunk(idx):
            if idx % 2 == 0:
                # descending
                xs = list(range(idx, -1, -1))
                ys = copy(xs)
                ys.reverse()
                return list(zip(xs, ys))

            else:
                # ascending
                xs = list(range(0, idx+1))
                ys = copy(xs)
                ys.reverse()
                return list(zip(xs, ys))

        def get_chunks(dim):
            return [*map(gen_chunk, range(dim))]

        def get_rchunks(chunks, dim):
            rchunks = copy(chunks[:-1])
            rchunks.reverse()
            return [[(x[0]+idx, x[1]+idx) for x in chunk] for idx, chunk in enumerate(rchunks, 1)]

        dim = len(matrix)
        chunks = get_chunks(dim)
        rchunks = get_rchunks(chunks, dim)
        output = [matrix[x][y] for x, y in chain(* (chunks + rchunks))]
        return output
