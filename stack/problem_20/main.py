from solution import Solution

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: input list and target
        s = lines[i].strip('"')

        # Second line: expected output
        expected = lines[i+1] == "True"

        # Run
        result = sol.isValid(s)

        # Print result
        print(f"Input: string={s}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

if __name__ == "__main__":
    main()
