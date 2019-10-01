from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(idx):
            if idx == len(s) // 2:
                return
            ridx = (len(s) - 1) - idx
            s[idx], s[ridx] = s[ridx], s[idx]
            helper(idx+1)
        helper(0)
        return s
