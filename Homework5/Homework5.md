## 算法分析与复杂性理论 - Homework 5

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 5. 最长回文子串

#### 题目：

> 给定一个字符串s，找到s中最长的回文子串。
>
> 注：回文串是指左右对称的字符串。

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework5/figures/1.jpg)

#### 代码：

```python
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
```

#### 算法思路描述：(时间复杂度O(n ^ 2)，空间复杂度O(n ^ 2))

1. 利用动态规划的思想，首先创建二维数组*dp*，其中的每个元素`dp[i][j]`表达的是第i个字符到第j个字符所组成的子串，是否为回文串，若是则`dp[i][j]=True`，反之则为`False`
2. 初始化dp数组，将其构建为`n x n`大小的二维数组，同时将`dp[i][i]`都初始化为`True`，因为每个单独的字符都可以看作是长度为1的回文串，进而思考状态转移方程：
   * 若一个回文串左右两个字符相同，那么加上左右两个字符之后组成的更长的字符串，也是回文串；反之若左右两个字符不相同，那么无法构成更长的回文串，状态转移方程为：`dp[i][j] = dp[i+1][j-1] * (s[i] == s[j])`
   * 特殊情况下，单个字符和空字符也可以看作是回文串，当某个字符左右为两个相同字符时或者相邻两个字符相同时，可构成更长的回文串，方程为：`dp[i][j] = (s[i] == s[j]) if j-i <= 2`
3. 明确状态定义，状态初始化，状态转移方程之后即可编写代码，此处利用双重循环，外循环控制构造子串的长度，内循环控制子串的起始位置，记起始位置为`i`，终止位置为`j`，同时判断终止位置是否越界，越界则直接出循环。根据状态转移方程对`dp`数组进行更新，同时记录最短的回文串长度及其起点，最终返回`s[start:start+maxLen]`即可，即对应的最短回文串



### LeetCode 64. 最小路径和

#### 题目：

> 给定一个包含非负整数的 `*m* x *n*` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
>
> **说明：**每次只能向下或者向右移动一步。

#### 示例截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework5/figures/0.jpg)

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework5/figures/2.jpg)

#### 代码：

```python
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
```

#### 算法思路描述：（时间复杂度O(n ^ 2)，空间复杂度O(n ^ 2)）

1. 利用动态规划的思想，首先创建二维数组*dp*，其中的每个元素`dp[i][j]`表达的是从地图左上角起点`(0, 0)`走到当前位置`(i, j)`的最小路径和
2. 初始化状态数组，首先`dp[0][0] = grid[0][0]`初始化起点最小路径和，由于每次只能向右或者向下走，所以地图中的每个格子只能够从他的上面一格或者是左边一格走过来，所以地图的第一行格子的最小路径和一定是他本身的路径长度加上相邻左边格子的最小路径和，即`dp[0][j] = dp[0][j-1] + grid[0][j]`，同理，地图的第一列格子的最小路径和一定时他本身的路径长度加上相邻上边格子的最小路径和，即`dp[i][0] = dp[i-1][0] + grid[i][0]`
3. 状态转移方程为：`dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]`，即每个格子的最小路径和，等于他相邻上边的格子和相邻左边的格子的最小路径和的最小值，加上他本身的路径长度
4. 最后返回地图右下角的最小路径和即可，即`dp[m-1][n-1]`，即表示从左上角到右下角的最短路径和长度



### LeetCode 120. 三角形最小路径和

#### 题目：

> 给定一个三角形 triangle ，找出自顶向下的最小路径和。
>
> 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
>

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework5/figures/3.jpg)

#### 代码：

```python
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
```

#### 算法思路描述：（时间复杂度O(n ^ 2)，空间复杂度O(n ^ 2)）

1. 利用动态规划的思想，首先创建二维数组*dp*，其中的每个元素`dp[i][j]`表达的是从三角形的顶部走到当前元素`(i,j)`的最小路径和

2. 状态初始化为：`dp[0][0] = triangle[0][0]`，状态转移的过程为：上一步位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1，所以对于每一个节点来说，存在以下三种状态转移方式：

   * 当前节点位于第一列（三角形的左边界）：则只能够由当前节点的上一行同一列的节点转移过来，即`dp[i][j] = dp[i-1][j]`
   * 当前节点位于三角形的右边界：则只能够由当前节点的上一行前一列的节点转移过来，即`dp[i][j] = dp[i-1][j-1]`
   * 当前节点在三角形内部：可以由当前节点的上一行中的同一列，或者前一列的节点转移过来，即`dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])`，取两者最小值作为最短路径和

3. 最终，取最底层（最后一行）中所有节点的最小路径和，值最小的作为从顶向下的三角形最小路径和

   

   

