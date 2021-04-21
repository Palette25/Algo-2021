def maxProfit(f):
	'''
	  f (n x m list)
	'''
	n, m = len(f)-1, len(f[0])-1
	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
	
	for i in range(1, n+1):
		for j in range(m+1):
			for k in range(j+1):
				dp[i][j] = max(dp[i][j], f[i][k] + dp[i-1][j-k])
	
	return dp[n][m]

# Test
if __name__ == '__main__':
	f = [[0,0,0,0,0],
		 [0,5,6,7,8],
		 [0,9,10,11,12],
		 [0,13,14,15,16]]

	p = maxProfit(f)

	print('Input f:', f)
	print('The max profit: ', p)