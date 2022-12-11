#T:O(n^2), S:O(n^2)
class Solution:
    def validPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1:
            return 0
        if m <= 1 or n <= 1:
            return 0 if grid[m-1][n-1] == 1 else 1

        dp = [[0]* n for _ in range(m)]
        for i in range(m):
            if grid[i][0] == 1:
                dp[i][0] = 0
                break
            dp[i][0] = 1

        for i in range(n):
            if grid[0][j] == 1:
                dp[0][j] = 0
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1,n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
