class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for k in range(1, n):
            for i in range(0, n - k):
                j = i + k
                remove_i = piles[i]
                remove_j = piles[j]

                if (n - (k + 1)) % 2 == 0:  # alex's move
                    dp[i][j] = max(remove_i + dp[i + 1][j],
                                   remove_j + dp[i][j - 1])
                else:
                    dp[i][j] = min(- remove_i + dp[i + 1][j],
                                   - remove_j + dp[i][j - 1])

        return dp[0][n - 1] > 0