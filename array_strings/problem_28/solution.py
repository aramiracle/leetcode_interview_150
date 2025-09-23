class Solution(object):
    def strStr(self, haystack, needle):
        """
        Return the index of the first occurrence of `needle` in `haystack`, 
        or -1 if `needle` is not part of `haystack`.

        Args:
            haystack (str): The main string in which to search.
            needle (str): The substring to find within `haystack`.

        Returns:
            int: The index of the first occurrence of `needle` in `haystack`, 
                 or -1 if not found.
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1