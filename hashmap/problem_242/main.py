from solution import Solution

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: input list
        s, t = [string.strip().strip('"') for string in lines[i].split(";")]

        # Second line: expected output
        expected_str = lines[i+1].strip()
        expected = expected_str == "True"

        # Run
        result = sol.isAnagram(s, t)

        # Print result
        print(f"Input: word 1={s}, word 2={t}")
        print(f"Result: '{result}'")
        print(f"Expected: '{expected}'")
        print(f"Pass: {result == expected}\n")

if __name__ == "__main__":
    main()