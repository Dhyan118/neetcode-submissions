class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):

                dp[i] = min(dp[i], dp[i - c] + 1)

                # coin = 4
                #i = 7
                # dp[7] = 1 + dp[3]

        return dp[amount] if dp[amount] != float("inf") else -1
