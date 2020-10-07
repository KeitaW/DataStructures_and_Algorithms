from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(int)
        for char in list(s):
            char_count[char] += 1
        unique_char_loc = [
            (s.index(char), char) for char, value in char_count.items() if value == 1
        ]
        if not unique_char_loc:
            return -1
        return sorted(unique_char_loc)[0][0]

