class Solution(object):
    def isHappy(self, n):
        """
        Determine if a number is a happy number.

        A happy number is defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits,
        and repeat the process until the number equals 1 (where it will stay),
        or it loops endlessly in a cycle which does not include 1.

        Args:
            n (int): The positive integer to check.

        Returns:
            bool: True if n is a happy number, False otherwise.
        """
        digits_set = set()

        while True:
            digits = self.find_digits(n)
            n = self.sum_square(digits)

            if n == 1:
                return True
            if digits in digits_set:
                return False
            else:
                digits_set.add(digits)

    def sum_square(self, digits):
        """
        Calculate the sum of squares of the given digits.

        Args:
            digits (iterable of int): A sequence of digits.

        Returns:
            int: Sum of the squares of the digits.
        """
        s = 0
        for digit in digits:
            s += digit ** 2
        return s

    def find_digits(self, num):
        """
        Extract digits of a number as a tuple, from least significant to most significant.

        Args:
            num (int): The number from which to extract digits.

        Returns:
            tuple of int: Digits of the number in order from least significant to most significant.
        """
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        return tuple(digits)
