## 算法分析与复杂性理论 - Homework 6

#### 姓名：陈明亮

#### 学号：2001212817



### 1. 完全背包问题

#### 题目：

> 一个旅行者随身携带一个背包，可以放入背包的物品有n种，每种物品的重量和价值分别是wi和vi，i=1, .... , n. 
>
> 如果背包的最大容量限制是b，怎样选择放入背包的物品以使得背包的价值最大？



#### 算法思路描述：(时间复杂度O()，空间复杂度O())

1. 本题为完全背包问题，即每种物品具有多个，一种物品可以多个放进背包中。通过求解放入前`i-1`种物品的最大价值，即可递推得到放入前`i`种物品的最大价值

2. 目标函数：`max(k1 * v1 + .... + kn * vn)`，约束条件：`(k1 * w1 + ... + kn * wn) <= b`

3. 采用动态规划求解本题，首先构建二维数组`dp`，其中每个元素`dp[i][j]`表示在背包容量剩余`j`时放入前`i`种物品的最大价值，状态初始化为：当放入物品种类数为0时收益必定为0；当背包容量为0时收益为0。状态转移存在以下两种情况：

   * 当需要放入的第`i`种物品的单个重量`wi > j`时，无法放下该种物品，此时最大价值应该与只放`i-1`种物品的最大价值保持相同：

     `dp[i][j] = dp[i-1][j], if wi > j`

   * 当目前背包容量`j`至少可以容纳一件第`i`种物品，至多可以容纳`k`件第`i`种物品时，那么此时需要比较放入不同数量时所产生的最大价值：

     `dp[i][j] = max(dp[i-1][j-c*wi] + c*vi), while 0 <= c <= k `



#### 代码：

```python
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
    
    return dp[n][b]
```



#### 运行截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework6/figures/1.jpg)



### 2. 投资问题

#### 题目：

> 设有m元钱，n项投资，函数fi(x)表示将x元钱投入到第i项项目所产生的效益，i=1,...,n. 
>
> 问：如何分配这m元钱，使得投资的总效益最高？



#### 算法思路描述：（时间复杂度O()，空间复杂度O()）

1. 题目中可以看到，我们需要使用m元钱去投资项目，不同的项目投资不同的钱产生的效益不同，我们最终必须取得最大化的收益，本质上也是一个最优化问题；我们也可以采取动态规划的解法求解最大收益值
2. 考虑到存在的变量有两个：钱数与项目数，采用二位的`dp`数组，其中每一项状态`dp[i][j]`表示的是对于前i个项目我总共投资j元钱之后所产生的收益值；状态的初始化过程需要考虑临界条件：当投资0个项目时必定产生0收益 -- `dp[0][j] = 0`，当使用0元投资项目时必定产生0收益 -- `dp[i][0] = 0`
3. 状态转移方程很简单，为：`dp[i][j] = max{f[i][k] + dp[i-1][j-k]}, while 0 <= k <= j`，即每次投资第i个项目时，我需要考虑对其投资k元时的收益，并取最大收益值，其中`0 <= k <= j`，如此一来就能取得全局收益最大化的解
4. 最终`dp[n][m]`即为使用m元钱投资n项之后产生的最大收益值



#### 代码：

```python
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
```



#### 运行截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework6/figures/2.jpg)



