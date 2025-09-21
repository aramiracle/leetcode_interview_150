class Solution(object):
    def __init__(self):
        self.roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

    def romanToInt(self, s):
        """
        Convert a Roman numeral string to its integer representation.

        Args:
            s (str): A valid Roman numeral string (1 <= value <= 3999).

        Returns:
            int: The integer value corresponding to the Roman numeral.
        """
        total = 0
        prev = 0
        for ch in reversed(s):
            curr = self.roman_dict[ch]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total
