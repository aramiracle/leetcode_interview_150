from solution import Solution

def parse_list(s):
    """Convert a string like '[2, 7, 11, 15]' into a Python list of ints."""
    s = s.strip().strip("[]")
    return [int(x.strip()) for x in s.split(",")]

def parse_list_string(s: str):
    """Convert a string like '["a", "b"]' into a Python list of strings."""
    s = s.strip()
    if s == "[]":
        return []
    return [x.strip().strip('"').strip("'") for x in s[1:-1].split(",")]

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: input list and target
        nums = parse_list(lines[i])

        # Second line: expected output
        expected = parse_list_string(lines[i+1])

        # Run
        result = sol.summaryRanges(nums)

        # Print result
        print(f"Input: nums={nums}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

if __name__ == "__main__":
    main()
