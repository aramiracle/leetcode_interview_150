class Solution(object):
    def maxProfit(self, prices):
        """
        Calculate the maximum profit from a single buy-sell transaction 
        using a divide-and-conquer approach.

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: The maximum profit achievable. Returns 0 if no profit is possible.
        """
        if prices:
            return self.divide_and_conquer(prices, 0, len(prices) - 1)
        else:
            return 0

    def divide_and_conquer(self, prices, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        # max profit in left half
        left_profit = self.divide_and_conquer(prices, left, mid)
        # max profit in right half
        right_profit = self.divide_and_conquer(prices, mid + 1, right)

        # max profit crossing the middle
        min_left = min(prices[left:mid+1])
        max_right = max(prices[mid+1:right+1])
        cross_profit = max_right - min_left

        return max(left_profit, right_profit, cross_profit)
