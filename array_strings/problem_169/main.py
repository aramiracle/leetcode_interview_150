from solution import Solution

def parse_list(s: str):
    """Convert a string like '[1,2,3]' into a Python list of ints."""
    s = s.strip()
    if s == "[]":
        return []
    return [int(x.strip()) for x in s.strip("[]").split(",")]

def main():
    # Read test cases from file
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    sol = Solution()

    # Iterate through test cases
    for i in range(0, len(lines), 2):
        # First line: inputs
        nums_str = lines[i].strip()
        nums = parse_list(nums_str)

        # Second line: expected output
        expected_maj_str = lines[i+1].strip()
        expected_maj = int(expected_maj_str)

        # Run 
        maj = sol.majorityElement(nums)

        # Print result
        print(f"Input: nums={nums_str}")
        print(f"Result: {maj}")
        print(f"Expected: {expected_maj}")
        print(f"Pass: {maj == expected_maj}\n")

if __name__ == "__main__":
    main()
