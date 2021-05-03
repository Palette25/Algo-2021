def maximalRectangle(self, matrix: List[List[str]]) -> int:
    # Init dp as matrix[i][j]'s number of left continuous 1
    m = len(matrix)
    if m == 0: return 0
    n = len(matrix[0])
    res = 0

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if j > 0:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 1
            # Calculate max area
            width = dp[i][j]
            k = i
            while k >= 0:
                if dp[k][j] == 0: break
                width = min(width, dp[k][j])
                res = max(res, width*(i-k+1))
                k -= 1

    return res