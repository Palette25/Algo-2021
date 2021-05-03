## 算法分析与复杂性理论 - Homework 7

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 85.  最大矩形

#### 题目：

> 给定一个仅包含 `0` 和 `1` 、大小为 `rows x cols` 的二维二进制矩阵，找出只包含 `1` 的最大矩形，并返回其面积。



#### 示例：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework7/figures/0.jpg)

上述示例中的最大矩形面积为`6`



#### 代码：

```python
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
```



#### 算法思路描述：(时间复杂度O(n * m^2)，空间复杂度O(m * n))

1. 运用动态规划求解此题，首先构建二维`dp`数组，并且`dp[i][j]`表示的含义为：从左侧开始，以当前元素`matrix[i][j]`结尾的由1构成的最长连续序列长度，对应的状态转移方程为：`dp[i][j] = dp[i][j-1] + 1`，当当前元素本身就为0时，`dp[i][j] = 0`
2. 构建完`dp`数组之后，对于每一个元素`matrix[i][j]`，我们需要获得其作为矩形右下角时，所可以获得的最大矩形面积`maxArea`，并且最终返回当前矩阵的最大矩形面积。故此我们需要进行自底向上的遍历，对于元素`matrix[i][j]`，其左边最长的连续由1构成的序列长度为`dp[i][j]`，当前行数为`k`，每次取当前构成矩形的最小宽度`width = min(width, dp[k][j])`，如果遇到`dp[k][j] == 0`则直接退出循环，反之则获取到当前的最大矩形面积`maxArea = width * (i-k+1)`，其中`i`为原始元素所在行，如此循环往复，最终肯定可以获取到最大矩形面积
3. 优化：
   * 可以在计算最大矩形面积的同时，初始化`dp`数组，以减少运行时间
   * 自底向上计算最大矩形面积，遇到0元素直接退出循环，减少运行时间



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework7/figures/1.jpg)



### LeetCode 152. 乘积最大子数组

#### 题目：

> 给你一个整数数组 `nums` ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



#### 代码：

```python
def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_dp, min_dp = [0] * n, [0] * n

        # init dp
        max_dp[0] = min_dp[0] = nums[0]

        for i in range(1, n):
            min_dp[i] = min(nums[i], min(
                			min_dp[i-1] * nums[i], max_dp[i-1] * nums[i]))
            max_dp[i] = max(nums[i], max(
                			min_dp[i-1] * nums[i], max_dp[i-1] * nums[i]))
        
        res = max_dp[0]
        for ele in max_dp:
            res = max(res, ele)
        
        return res
```



#### 算法思路描述：（时间复杂度O(n)，空间复杂度O(n)）

1. 与相加之和最大子数组不同的是，乘积最大的子数组中可以包含负数，并且当两个负数相乘时，甚至可以获得当前最大的乘积结果。因此，此题需要开辟两个一维的`dp`数组，一个负责存储以当前元素结尾的左侧子数组的乘积最大值，另一个存储以当前元素结尾的左侧子数组的乘积最小值，状态初始化为：`min_dp[0] = max_dp[0] = nums[0]`
2. 需要注意的是，乘积最大值可以从之前的乘积最小值乘以一个负数从而产生，反过来乘积最小值也可以从之前的乘积最大值乘以一个负数产生，所以状态转移方程需要写成：
   * `min_dp[i] = min(nums[i], min_dp[i-1]*nums[i], max_dp[i-1]*nums[i])`
   * `max_dp[i] = max(nums[i], min_dp[i-1]*nums[i], max_dp[i-1]*nums[i])`
3. 最终我们只需要在存储乘积最大值的数组里边寻找最大值即可，作为最大子数组的乘积即可



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework7/figures/2.jpg)



