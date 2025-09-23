from solution import Solution

def parse_list_string(s: str):
    """Convert a string like '["a","b"]' into a Python list of strings."""
    s = s.strip()
    if s == "[]":
        return []
    return [x.strip().strip('"').strip("'") for x in s.split(";")]

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: input list
        string = parse_list_string(lines[i])

        # Second line: expected output
        expected_str = lines[i+1].strip()
        expected = bool(expected_str)

        # Run
        result = sol.isPalindrome(string)

        # Print result
        print(f"Input: string={string}")
        print(f"Result: '{result}'")
        print(f"Expected: '{expected}'")
        print(f"Pass: {result == expected}\n")

if __name__ == "__main__":
    main()