def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)

    max_dp, min_dp = [0] * n, [0] * n

    # init dp
    max_dp[0] = min_dp[0] = nums[0]

    for i in range(1, n):
        min_dp[i] = min(nums[i], min(min_dp[i-1] * nums[i], max_dp[i-1] * nums[i]))
        max_dp[i] = max(nums[i], max(min_dp[i-1] * nums[i], max_dp[i-1] * nums[i]))
    
    res = max_dp[0]
    for ele in max_dp:
        res = max(res, ele)
    
    return res