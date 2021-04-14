class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Use dynamic programming
        # dp[i][j] means: the minimum path's sum from top to node(i, j)
        m = len(triangle)

        dp = [[0] * m for i in range(m)]
        dp[0][0] = triangle[0][0]

        for i in range(1, m):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])
                
                dp[i][j] += triangle[i][j]
        
        # Find minimum sum at the last level
        res = dp[m-1][0]
        for i in range(1, m):
            res = min(res, dp[m-1][i])
        
        return res