class Solution:

    def lengthOfLongestSubstring(self, string: str) -> int:
        """Function that returns the LSWRC.

        Longest Substring Without Repeating Characters (LSWRC)
        """
        # Function that returns the longest substring
        #
        NO_OF_CHARS = 256
        n = len(string)
        # Initialize the visited array as -1, -1 is used to indicate
        # that character has not been visited yet.
        visited = [-1] * NO_OF_CHARS
        # Mark the first character as visited by storing the index of
        # first character in visited array.
        visited[ord(string[0])] = 0
        # Start from the second character. First character is already
        # processed (cur_len and max_len are initialized as 1, and 
        # visited[ord(string[0])] is set 
        cur_len = 1     # To store the length of current string
        max_len = 1     # To store the longest substring
        prev_index = 0  # To store the previous index
        for i in range(1, n):
            prev_index = visited[ord(string[i])]

            # If the current character is not present in the already
            # processed substirng or it is not part of the current
            # longest substring, then do cur_len++
            if prev_index == -1 or (i - cur_len > prev_index):
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = i - prev_index
            visited[ord(string[i])] = i
        if cur_len > max_len:
            max_len = cur_len
        return max_len