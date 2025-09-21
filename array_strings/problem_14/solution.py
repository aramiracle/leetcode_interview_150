class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Find the longest common prefix among an array of strings.

        Args:
            strs (List[str]): List of strings.

        Returns:
            str: The longest common prefix string.
        """
        prefix = ""
        max_count = min([len(s) for s in strs])
        for i in range(max_count):
            check_char = strs[0][i]
            for j in range(1, len(strs)):
                char = strs[j][i]
                if char != check_char:
                    return prefix
            prefix += check_char
        return prefix
