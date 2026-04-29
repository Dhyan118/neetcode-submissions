class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string
        dp[1] = 1  # First character (already checked it's not '0')

        # Iterate through the string
        for i in range(2, n + 1):
            # Check single digit (last one)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check two digits (last two)
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        # The last element holds the total number of ways
        return dp[n]