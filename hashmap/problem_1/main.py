from solution import Solution

def parse_list(s):
    """Convert a string like '[2, 7, 11, 15]' into a Python list of ints."""
    s = s.strip().strip("[]")
    return [int(x.strip()) for x in s.split(",")]

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: input list and target
        nums_str, target_str = lines[i].split(";")
        nums = parse_list(nums_str)
        target = int(target_str.strip())

        # Second line: expected output
        expected = set(parse_list(lines[i + 1]))

        # Run
        result = set(sol.twoSum(nums, target))

        # Print result
        print(f"Input: nums={nums}, target={target}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

if __name__ == "__main__":
    main()
