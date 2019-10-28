class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for idx in range(0, len(haystack) - len(needle) + 1):
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        return -1
