class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Applying 2 pointer method

        # Initialize left and right pointers, left(slow), right(fast)
        l, r = 0, 0
        # Initialize output variable
        max_profit = 0

        # Iterating through each element until reach the last element
        while r < len(prices):
            # If future price is greater than past price then profit
            if prices[l] < prices[r]:
                # Update max_profit with each profit to make sure we capture the
                # largest profit
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                l = r # if we find price lower than our past price, 
                # we should move that as it is our new low price
            r += 1 # move right pointer by 1
        return max_profit