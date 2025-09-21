from solution import Solution

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: inputs
        print(lines[i])
        roman_string = lines[i].strip('"')

        # Second line: expected outputs
        num_str = lines[i+1]
        num_expected = int(num_str.strip())

        # Run
        num = sol.romanToInt(roman_string)

        # Print result
        print(f"Input: string={roman_string}")
        print(f"Result: {num}")
        print(f"Expected: {num_expected}")
        print(f"Pass: {num == num_expected}\n")

if __name__ == "__main__":
    main()