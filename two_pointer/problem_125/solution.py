class Solution(object):
    def isPalindrome(self, s):
        """
        Check if a given string is a palindrome, considering only 
        alphanumeric characters and ignoring case.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the processed string is a palindrome, 
                  False otherwise.
        """
        s = ''.join([i for i in s if i.isalnum()])
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False
