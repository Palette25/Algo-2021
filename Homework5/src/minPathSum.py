class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Use dynamic programming
        # dp[i][j] means: from start to (i, j), the minimum number sum
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]

        # Init states
        dp[0][0] = grid[0][0]
        # Init first column states
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # Init first row states
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Apply state transfer equation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]