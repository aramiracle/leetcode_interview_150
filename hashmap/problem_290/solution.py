class Solution(object):
    def wordPattern(self, pattern, s):
        """
        Check if a string `s` follows the same pattern as `pattern`.

        Args:
            pattern (str): A string of lowercase letters representing the pattern.
            s (str): A space-separated string of words to match against the pattern.

        Returns:
            bool: True if `s` follows the same pattern as `pattern`, otherwise False.
        """
        words = s.split()
        return (len(pattern) == len(words) and 
                len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words)))
