## 算法分析与复杂性理论 - Homework 10

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 787.  K站中转内最便宜的航班

#### 题目：

> 有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。
>
> 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。
>



#### 代码：

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # DP
        # dp[i][j] means src takes j transfers to get to i destination's min cost
        MAX_VALUE = 2**31-1
        dp = [[MAX_VALUE] * (k+1) for _ in range(n)]

        # Init src direct cities
        for pair in flights:
            if pair[0] == src:
                dp[pair[1]][0] = pair[2]
        
        # Init zero stops
        for i in range(k+1):
            dp[src][i] = 0
        
        for i in range(1, k+1):
            for flight in flights:
                if dp[flight[0]][i-1] != MAX_VALUE:
                    dp[flight[1]][i] = min(dp[flight[1]][i], dp[flight[0]][i-1] + flight[2])

        if dp[dst][k] == MAX_VALUE:
            return -1
        else:
            return dp[dst][k]
```



#### 算法思路描述：(时间复杂度O(n * k))，空间复杂度O(n^2))

1. 利用动态规划的思想求解本题，首先定义状态`dp[i][j]`，表示的是：`从出发点src到i的路程中，运行最大中转次数为j，所需要的最小开销`，初始化`dp`数组为`n * (k+1)`，同时初值都为最大值`MAX_VALUE`，此处的最大值为`int`类型上界
2. 然后做进一步的初始化，对于给定的飞行行程列表`flights`，我们可以知道`src`直达的城市所需的最小价格；同时从`src`到其自身的价格必为0
3. 状态转移方程为`dp[i][j] = min(dp[i][j], dp[k][j-1] + cost[k][i])`，其中`城市k`到`城市i`之间的开销为`cost[k][i]`，由此就能够计算出，最终从`src`到`dst`，最多经过`k`次中转所需的最小开销



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework10/figures/1.jpg)



### LeetCode 934.  最短的桥

#### 题目：

> 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
>
> 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
>
> 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）
>



#### 代码：

```python
class Solution:
    def dfs(self, grid, m, n, i, j, queue):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
            return
        # Trun the first island's element into 2
        grid[i][j] = 2
        # Push Tuple (x, y, step) into queue
        queue.append((i, j, 0))

        # UP DOWN LEFT RIGHT Searching
        self.dfs(grid, m, n, i-1, j, queue)
        self.dfs(grid, m, n, i+1, j, queue)
        self.dfs(grid, m, n, i, j-1, queue)
        self.dfs(grid, m, n, i, j+1, queue)


    def shortestBridge(self, grid: List[List[int]]) -> int:
        # DFS: find the first island
        m, n = len(grid), len(grid[0])
        queue = []
        find = False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, m, n, i, j, queue)
                    find = True
                    break

            if find: break
        
        # BFS: let first island expand and find the min distance
        #      to the second island
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while len(queue) > 0:
            peek = queue[0]
            queue.pop(0)

            x = peek[0]
            y = peek[1]
            step = peek[2]

            # UP DOWN LEFT RIGHT Expanding
            for i in range(4):
                new_x = x + dir[i][0]
                new_y = y + dir[i][1]

                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n \
                    or grid[new_x][new_y] == 2:
                    continue
                
                if grid[new_x][new_y] == 1:
                    return step
                
                # grid[new_x][new_y] == 0 -> combine into one island
                grid[new_x][new_y] = 2
                queue.append((new_x, new_y, step + 1))
        
        return -1
```



#### 算法思路描述：（时间复杂度O(n ^ 2)，空间复杂度O(n^  2)）

1. 利用深度优先搜索DFS，首先找到第一个岛屿，并且将该岛屿上的元素全部变为2，采用的是递归形式的深度优先搜索，并且每一次都是从上下左右四个方向进行搜索。每次搜索都将该岛屿的元素`push`进队列`queue`中
2. 利用广度优先搜索`BFS`，对第一个岛屿的元素队列`queue`进行遍历，每次取队列的头部元素进行操作。对于每个岛屿上的元素，同样按照四个方向进行搜索，如果找到了值为1的元素，则找到了另一个岛屿，此时直接返回`step`，此处的`step`为当前的队列头部元素与第一个岛屿之间的距离；反之如果找到值为0的元素，则把他加入到第一个岛屿的`领土`里，并且他跟第一个岛屿之间的距离等于当前头部元素的距离+1
3. 最终，我们就能找到两个岛屿之间的最小距离



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework10/figures/2.jpg)



### LeetCode 692 .  前K个高频单词

#### 题目：

> 给一非空的单词列表，返回前 *k* 个出现次数最多的单词。
>
> 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。



#### 代码：

```python
class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre
    def __gt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = collections.Counter(words)
        heap = []

        for word, fre in cnt.items():
            heapq.heappush(heap, Word(word, fre))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort()
        return [x.word for x in heap]
```



#### 算法思路描述：（时间复杂度O(nlogn)，空间复杂度O(n)）

1. 对于每个单词，我们构建单词类`Word`，其拥有两个属性`word, fre`，其中`word`存储单词内容，`fre`存储其出现次数。同时，我们必须为该类定义内置的小于函数`__lt__`，该函数首先看两个单词的出现频率，若不相等，则直接比较频率高低，在降序排序时，频率高的单词应该在频率低的单词的左侧，即频率高的单词要`小`；若相等，则直接比较单词大小，字典序大的单词就应该更`大`，排在列表的右侧
2. 通过构建最小堆的方法，控制最小堆的大小为K，这样我们就能够返回正确排序顺序下的，出现频率最高的K个元素



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework10/figures/3.jpg)

