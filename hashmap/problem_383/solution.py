class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        Determine if the ransom note can be constructed using the letters from the magazine.

        Args:
            ransomNote (str): The string representing the ransom note to construct.
            magazine (str): The string representing the available letters in the magazine.

        Returns:
            bool: True if ransomNote can be constructed from magazine, False otherwise.
        """
        dictionary = {}
        alphabet_set = set(ransomNote + magazine)

        for char in alphabet_set:
            dictionary[char] = 0
        
        for char in magazine:
            dictionary[char] += 1

        for char in ransomNote:
            dictionary[char] -= 1
            if dictionary[char] < 0:
                return False

        return True
