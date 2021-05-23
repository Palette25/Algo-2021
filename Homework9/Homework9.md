## 算法分析与复杂性理论 - Homework 9

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 240.  搜索二维矩阵II

#### 题目：

> 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
>
> 每行的元素从左到右升序排列。
> 每列的元素从上到下升序排列。



#### 代码：

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0 : return False
        n = len(matrix[0])
        if n == 0 : return False

        # Init right upper corder location
        row, col = 0, n-1

        while row < m  and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True

        return False
```



#### 算法思路描述：(时间复杂度O(m + n)，空间复杂度O(1))

1. 由于当前矩阵内部，每行元素从左到右是升序排列，每列元素从上到下是升序排列，那么当前矩阵的右上角元素的左侧元素均小于它，下侧元素均大于它
2. 通过初始化下标，那么我们可以从矩阵的右上角元素`matrix [row][col]`开始搜索，其中`row = 0, col = n-1`，构建遍历循环，循环条件为元素的下标不越界，当`matrix[row][col] > target`时，`col--`，当`matrix[row][col] < target`时，`row++`，当`matrix[row][col] == target`，直接返回`True`
3. 如果循环内没有找到对应元素，直接返回`False`



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework9/figures/1.jpg)



### LeetCode 347.  前K个高频元素

#### 题目：

> 给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。



#### 代码：

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for key, val in count.items():
            if len(heap) >= k:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [item[1] for item in heap]
```



#### 算法思路描述：（时间复杂度O(nlogk)，空间复杂度O(k)）

1. 通过构建最小堆的方法，只存储当前数组中出现频率最高的前K个元素，堆顶为最小元素，最终返回堆内的K个元素对应的`key`值即可
2. 首先利用`collection.Counter`进行数组中元素出现次数的统计，遍历数组元素，同时维护最小堆`heap`，当堆内元素个数小于k时，直接将当前元素`push`进堆中；反之当堆内元素个数大于等于k时，如果当前元素的出现次数大于堆顶元素的出现次数时，将其与堆顶元素进行替换`replace`，更新最小堆
3. 最终返回堆内K个元素对应的`key`值即可，`python`中堆的操作借助了`heapq`库



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework9/figures/2.jpg)



### LeetCode 374 .  猜数字大小

#### 题目：

> 猜数字游戏的规则如下：
>
> 每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
> 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
> 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
>
> -1：我选出的数字比你猜的数字小 pick < num
> 1：我选出的数字比你猜的数字大 pick > num
> 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
> 返回我选出的数字。



#### 代码：

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        # check if pick == left or right
        if guess(left) == 0: return left
        if guess(right) == 0: return right

        while left <= right:
            mid = int((left + right) / 2)
            tmp = guess(mid)

            if tmp == -1:
                right = mid
            elif tmp == 1:
                left = mid
            else:
                return mid
        
        return -1
```



#### 算法思路描述：（时间复杂度O(logn)，空间复杂度O(1)）

1. 直接使用二分法进行查找，首先初始化搜索范围`[1, n]`，需要先判断该数字是否为范围边界，如果是的话直接返回
2. 否则进入`while`循环，每次取区间中点`mid = (left+right) / 2`，判断该中点与目标值的大小关系，如果`mid > target`则取当前区间的左半区间继续搜索，`mid < target`则取右半区间，反之则找到目标值直接返回即可



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework9/figures/3.jpg)

