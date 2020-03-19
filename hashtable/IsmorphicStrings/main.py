class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Given two strings s and t, determine if they are isomorphic.
        Two strings are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character while preserving the order of characters.
        No two characters may map to the same character but a character may map to itself.
        Example 1:
        Input: s = "egg", t = "add"
        Output: true
        Example 2:
        Input: s = "foo", t = "bar"
        Output: false
        
        Parameters
        ----------
        s : str
        t : str
        Assumption: len(s) == len(t)
        
        Returns
        -------
        bool
        """
        s_to_t = dict()
        t_to_s = dict()
        for char1, char2 in zip(s, t):
            if char1 in s_to_t:
                if s_to_t[char1] != char2:
                    return False
            else:
                s_to_t[char1] = char2
                if char2 in t_to_s and t_to_s[char2] != char1:
                    return False
                else:
                    t_to_s[char2] = char1
        return True

