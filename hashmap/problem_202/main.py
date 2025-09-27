from solution import Solution

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: input list and target
        num_str = lines[i].strip()
        num = int(num_str)

        # Second line: expected output
        expected = lines[i + 1].strip() == "True"

        # Run
        result = sol.isHappy(num)

        # Print result
        print(f"Input: number={num}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

if __name__ == "__main__":
    main()
