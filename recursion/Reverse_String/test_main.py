import pytest
from typing import List
from recursion.Reverse_String.main import Solution


def test_reverseString():
    solution = Solution()
    assert solution.reverseString(["h", "e", "l", "l", "o"]) == [
        "o", "l", "l", "e", "h"]
