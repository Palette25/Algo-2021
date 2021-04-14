class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Use dynamic programming
        # dp[i][j] means si to sj substring is palindrome or not
        n = len(s)
        maxLen, start = 1, 0

        if n < 2:
            return s

        dp = [[False] * n for i in range(n)]
        # Init states
        for i in range(n):
            dp[i][i] = True

        # dp
        # First loop to set substring's length
        for l in range(2, n+1):
            # Second loop to set substring's start index
            for i in range(n):
                j = l + i - 1
                if j >= n:
                    break
                # States transfer eqaution
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                                   
                # Update result
                if dp[i][j] and l > maxLen:
                    maxLen, start = l, i
       
        return s[start:start+maxLen]