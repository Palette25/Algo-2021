## 算法分析与复杂性理论 - Homework 1

#### 姓名：陈明亮
#### 学号：2001212817

### LeetCode 1. Two Sum

#### 题目：

> 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
>
> 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
>
> 你可以按任意顺序返回答案。
>

#### 测试截图：
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/0.jpg)

#### 代码：

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i in range(len(nums)) :
            if target - nums[i] not in dict :
                dict[nums[i]] = i
            else :
                return [dict[target-nums[i]], i]
```

#### 算法思路描述：

1. 为了避免暴力遍历算法时间复杂度过高(*O(n^2)*)，采用字典*dict*类型存储哈希表，最终的时间复杂度为*O(n)*，空间复杂度为*O(k)*。
2. 哈希表的存储思想为：将对应数组元素作为*key*，其出现的下标作为*value*。
3. 然后顺序遍历数组，看字典内是否具有与当前元素相加和为*target*的*key*，如果有的话，则直接返回当前下标与存储下标组成的*list*；否则就将当前元素及其下标作为*key-value*对存储进字典中。



### LeetCode 69. Sqrt(x)

#### 题目：

> 实现 int sqrt(int x) 函数。
>
> 计算并返回 x 的平方根，其中 x 是非负整数。
>
> 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
>

#### 测试截图：
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/1.jpg)

#### 代码：

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # If x is less than 2, return itself
        if x < 2 :
            return x
        # Binary Search to find square root
        left, right = 1, x // 2
        while left <= right :
            mid = (left + right) // 2
            if mid * mid > x :
                right = mid - 1
            else : 
                left = mid + 1
        return left - 1
```

#### 算法思路描述：

1. 使用二分法求解整数平方根，设定左边界*left*为1，右边界*right*为输入数*x*的除2取整，采用*while*循环查找，条件为左边界必须小于等于右边界。
2. 每次查找的过程中，都取当前区间的中点取整*mid*，判断其平方与*x*的大小关系，如果其平方值比*x*大，那么取当前区间的左半区间继续查找；否则取右半区间。
3. 最后返回*left-1*作为查找结果，因为跳出查找循环的条件是*left > right*，所以实际上左边界比多走了一步。



### LeetCode 70. Climbing Stairs

#### 题目：

> 设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。
>
> 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
>
> **注意：**给定 *n* 是一个正整数。

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/2.jpg)

#### 代码：

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = [1 for i in range(n+1)]
        
        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2]
        
        return F[n]
```

#### 算法思路描述：

采用动态规划的思想解题，状态转移方程为：
	

​	**F[0] = 1** 

​	**F[1] = 1**

​	**F[n] = F[n-1]+F[n-2] (n > 1)**

结合状态转移方程，通过初始化以及顺序遍历赋值的方式，构建斐波那契数列，最终即可返回对应n阶台阶的攀爬方法数*F[n]*。



