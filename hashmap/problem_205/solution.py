class Solution(object):
    def isIsomorphic(self, s, t):
        """
        Determine if two strings s and t are isomorphic.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if s and t are isomorphic, False otherwise.
        """
        return set(self.create_dict(s).values()) == set(self.create_dict(t).values())

    def create_dict(self, string):
        """
        Create a dictionary mapping each unique character in a string to the 
        indices where it appears.

        Args:
            string (str): Input string.

        Returns:
            dict: A dictionary where keys are characters and values are tuples 
                  of indices where those characters occur in the string.
        """
        string_dict = {}
        for i, char in enumerate(string):
            if char not in string_dict:
                string_dict[char] = [i]
            else:
                string_dict[char].append(i)
        return {char: tuple(indices) for char, indices in string_dict.items()}
