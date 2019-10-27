from typing import List


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        def parse_input(num: str):
            out = [*map(int, list(num))]
            out.reverse()
            return out

        a, b = parse_input(a), parse_input(b)

        def get_decimal(num: List[int]):
            decimal = 0
            for idx in range(len(num)-1, -1, -1):
                decimal += num[idx] * (2 ** idx)
            return decimal

        return bin(get_decimal(a) + get_decimal(b))[2:]
