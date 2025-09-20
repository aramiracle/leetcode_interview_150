from solution import Solution

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: inputs
        print(lines[i])
        string = lines[i].strip('"')

        # Second line: expected outputs
        length_str = lines[i+1]
        length_expected = int(length_str.strip())

        # Run
        length = sol.lengthOfLastWord(string)

        # Print result
        print(f"Input: string={string}")
        print(f"Result: {length}")
        print(f"Expected: {length_expected}")
        print(f"Pass: {length == length_expected}\n")

if __name__ == "__main__":
    main()