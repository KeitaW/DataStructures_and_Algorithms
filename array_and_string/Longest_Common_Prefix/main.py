from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def all_equal(elems):
            return len(set(elems)) == 1

        prefix = []
        for chars in zip(*strs):
            if all_equal(chars):
                prefix += chars[0]
            else:
                break
        return "".join(prefix)
