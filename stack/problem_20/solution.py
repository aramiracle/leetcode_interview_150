class Solution(object):
    def isValid(self, s):
        """
        Check if a string containing only parentheses is valid.

        Args:
            s (str): Input string containing only '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in mapping:
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
