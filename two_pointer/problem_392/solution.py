class Solution(object):
    def isSubsequence(self, s, t):
        """
        Determine if string `s` is a subsequence of string `t`.

        Args:
            s (str): The string to check as a subsequence.
            t (str): The target string in which to search.

        Returns:
            bool: True if `s` is a subsequence of `t`, False otherwise.
        """
        count = 0
        if s == "":
            return True
        for char in t:
            if s[count] == char:
                count += 1
            if count == len(s):
                return True
        return False