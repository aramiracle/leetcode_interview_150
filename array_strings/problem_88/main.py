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
        nums1_str, m_str, nums2_str, n_str = lines[i].split(';', 3)
        nums1 = parse_list(nums1_str)
        m = int(m_str.strip())
        nums2 = parse_list(nums2_str)
        n = int(n_str.strip())

        # Ensure nums1 has enough space
        if len(nums1) < m + n:
            nums1.extend([0] * (m + n - len(nums1)))

        # Second line: expected output
        expected = parse_list(lines[i + 1])

        # Run merge
        sol.merge(nums1, m, nums2, n)

        # Print result
        print(f"Input: nums1={nums1_str}, m={m}, nums2={nums2_str}, n={n}")
        print(f"Merged: {nums1}")
        print(f"Expected: {expected}")
        print(f"Pass: {nums1 == expected}\n")

if __name__ == "__main__":
    main()
