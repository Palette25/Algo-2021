def super_print(dp, m, n):
  for i in range(m):
    for j in range(n):
      print('  ' + str(dp[i][j]) + '  ', end='')
    print('')

  print('The max value: ', dp[m-1][n-1])


def complete_knapsack(w, v, b):
    '''
      w: n x 1 list
      v: n x 1 list
      b: int
    '''
    n = len(w)
    dp = [[0 for _ in range(b+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, b+1):
            k = 0
            while k * w[i-1] <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j-k*w[i-1]] + k*v[i-1])
                k += 1
    
    super_print(dp, n+1, b+1)
    return dp[n][b]


# Test
if __name__ == '__main__':
  w = [1,2,3,4,5]
  v = [10,20,30,40,50]
  b = 10
  print('w: ', w)
  print('v: ', v)
  print('b: ', b)

  complete_knapsack(w, v, b)