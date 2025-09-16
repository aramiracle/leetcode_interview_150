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
        print(lines[i].split(';'))
        nums_str, val_str = lines[i].split(';')
        print(nums_str, val_str)
        nums = parse_list(nums_str)
        val = int(val_str.strip())

        # Second line: expected outputs
        k_str, nums_str = lines[i+1].split(';')
        k_expected = int(k_str.strip())
        nums_expected = parse_list(nums_str)

        # Run
        k = sol.removeElement(nums, val)

        # Print result
        print(f"Input: val={val}, nums1={nums_str}")
        print(f"Implemeted: {k}, {nums[:k]}")
        print(f"Expected: {k_expected}, {nums_expected}")
        print(f"Pass: {k == k_expected and set(nums[:k]) == set(nums_expected[:k])}\n")

if __name__ == "__main__":
    main()