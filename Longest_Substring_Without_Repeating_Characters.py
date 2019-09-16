class Solution:

    def lengthOfLongestSubstring(self, string: str) -> int:
        if len(string) == 0: return 0
        NCHARS = 256
        # Initialize the visited array as -1, -1 is used to indicate
        # that character has not been visited yet.
        # Non-zero value corresponds to the index that the character appeared.
        visited = [-1] * NCHARS
        n = len(string)
        curr_len = 0  # To store the length of current string
        max_len = 1   # To store the longest substring
        for i in range(n):
            # prev_index here indicates the last index that the character observed.
            prev_index = visited[ord(string[i])]
            if (prev_index == -1) or (i - curr_len > prev_index):
                curr_len += 1
            else:
                curr_len = i - prev_index
            if curr_len > max_len:
                max_len = curr_len
            visited[ord(string[i])] = i
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("aab"))