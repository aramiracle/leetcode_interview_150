class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Calculate the length of the last word in a given string.

        Args:
            s (str): The input string containing words and spaces.

        Returns:
            int: The length of the last word in the string. Returns 0 if no word exists.
        """
        count = 0
        length = 0
        if s[len(s) - 1] == " ":
            while(s[len(s)- count - 1] == " " and count < len(s)):
                count += 1
        while(s[len(s) - count - 1] != " " and count < len(s)):
            count += 1
            length += 1
        return length