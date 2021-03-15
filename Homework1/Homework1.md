## 算法分析与复杂性理论 - Homework 1

#### 姓名：陈明亮
#### 学号：2001212817

### LeetCode 1. Two Sum
#### 测试截图：
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/0.jpg)
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/1.jpg)

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




### LeetCode 69. Sqrt(x)
#### 测试截图：
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/2.jpg)
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/3.jpg)

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




### LeetCode 70. Climbing Stairs
#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/4.jpg)
![img](https://github.com/Palette25/Algo-2021/blob/main/Homework1/figures/5.jpg)

#### 代码：

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current
```

#### 算法思路描述：

