from suboptimal_solution import Solution

def parse_list(s: str):
    """Convert a string like '[1,2,3]' into a Python list of ints."""
    s = s.strip()
    if s == "[]":
        return []
    return [int(x.strip()) for x in s.strip("[]").split(",")]

def main():
    with open("test_cases.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    sol = Solution()

    for i in range(0, len(lines), 2):
        # First line: inputs
        print(lines[i])
        prices_str = lines[i]
        prices = parse_list(prices_str)

        # Second line: expected outputs
        profit_str = lines[i+1]
        profit_expected = int(profit_str.strip())

        # Run
        profit = sol.maxProfit(prices)

        # Print result
        print(f"Input: nums={prices_str}")
        print(f"Result: {profit}")
        print(f"Expected: {profit_expected}")
        print(f"Pass: {profit == profit_expected}\n")

if __name__ == "__main__":
    main()