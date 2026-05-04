class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    
                    val = grid[i][j]
                    cost = 1 if val > 0 else 0
                    score = val

                    if i > 0:
                        if c >= cost and dp[i - 1][j][c - cost] != -1:
                            dp[i][j][c] = max(dp[i][j][c], dp[i - 1][j][c - cost] + score)

                    if j > 0:
                        if c>= cost and dp[i][j - 1][c - cost] != -1:
                            dp[i][j][c] = max(dp[i][j][c], dp[i][j - 1][c - cost] + score)

        res = max(dp[m - 1][n - 1])
        return res if res != -1 else -1