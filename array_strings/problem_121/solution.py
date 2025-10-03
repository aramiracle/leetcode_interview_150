class Solution(object):
    def maxProfit(self, prices):
        """
        Calculate the maximum profit from a single buy-sell transaction 
        in O(n) time and O(1) space.

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: The maximum profit achievable. Returns 0 if no profit is possible.
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
