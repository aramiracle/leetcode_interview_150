class Solution(object):
    def isAnagram(self, s, t):
        """
        Determine whether two strings are anagrams of each other.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if `t` is an anagram of `s`, otherwise False.
        """
        if set(s) != set(t):
            return False
        dictionary = {}
        alphabet_set = set(s)

        for char in alphabet_set:
            dictionary[char] = 0
        
        for char in s:
            dictionary[char] += 1

        for char in t:
            dictionary[char] -= 1

        for value in dictionary.values():
            if value:
                return False

        return True
