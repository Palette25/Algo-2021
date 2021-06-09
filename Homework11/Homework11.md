## 算法分析与复杂性理论 - Homework 11

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 743.  网络延迟时间

#### 题目：

> 有 n 个网络节点，标记为 1 到 n。
>
> 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
>
> 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
>



#### 代码：

```python
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = {node: [] for node in range(1, N+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N+1)}
        visited = [False] * (N+1)
        dist[K] = 0

        while True:
            # Find candidate
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not visited[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            visited[cand_node] = True
            # Update candidate's neighbors' distances
            for neighbor, dis in graph[cand_node]:
                dist[neighbor] = min(dist[neighbor], dist[cand_node] + dis)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
```



#### 算法思路描述：(时间复杂度O(n ^ 2)，空间复杂度O(n ^ 2))

1. 采用`Dijkstra`算法计算从起始节点`src`到所有其他节点的最短路径，然后再从其中选出长度最长的路径，作为该网络的延迟时间
2. `Dijkstra`算法的计算步骤为：
   * 首先根据信号传递时间列表`times`构建有向图的邻接表结构`graph`，记录从每个节点到其余节点的路径长度(所需时间)
   * 构建距离记录字典`dist`，其中每个`pair`对包括`(key, value)`键值对，其中的`key`为每个节点的编号，`value`为起始节点到该节点的最短路径长度，初始化为无穷`inf`
   * 构建访问数组`visited`，若已访问过该节点则置`True`，初始化为False
   * 首先让起始节点的最短路径距离初始化为0，即`dist[K] = 0`，然后构建循环，循环内部首先找到未访问过的，且路径长度最小的节点作为候选节点，如果没有找到候选节点，那么直接跳出循环`break`；反之则更新候选节点的邻居节点的最短路径长度`dist[neighbor] = min(dist[neighbor], dist[candidate] + dis)`，同时候选节点置为已访问状态
   * 最终，我们找到了所有节点的最短路径长度，然后取其中的最大值，如果最大值仍为无穷，则网络中有节点无法到达，返回-1；反之则直接返回网络最大延迟时间即可



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework11/figures/1.jpg)



### LeetCode 847.  访问所有节点的最短路径

#### 题目：

> 给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 
>
> graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。
>
> 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
>

#### 代码：

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # BFS
        n = len(graph)
        # Use binary sequence to represent current visit path
        # binary bit 1 is visited, 0 is not visited
        # pair(1 << x, x) means path that start from node x and currently only visit 
        # deque --> bi-direction queue
        queue = collections.deque((1 << x, x) for x in range(n))
        # dist[i][j] means the distance sum when current visit
        # node is j, and corresponding state is i
        dist = [[float('inf')] * n for _ in range(1 << n)]
        # init dist
        for i in range(n):
            dist[1 << i][i] = 0

        # Apply BFS
        while queue:
            # path_state, current_node
            state, cur = queue.popleft()
            d = dist[state][cur]
            # visit all nodes
            if state == (1<<n) - 1: 
                return d
            
            for neighbor in graph[cur]:
                # visit neighbor
                state_ne = state | (1 << neighbor)
                if d + 1 < dist[state_ne][neighbor]:
                    dist[state_ne][neighbor] = d + 1
                    queue.append((state_ne, neighbor))
        
        return -1
```



#### 算法思路描述：（时间复杂度O( )，空间复杂度O( )）

1. 首先我们使用一串二进制位对当前无向连通图中的节点的访问状态进行编码，即二进制串的长度为`n`，同时如果其第`i`位为1，那么表示节点`i`被访问过，反之为0，就代表没有被访问过
2. 我们定义路径的访问状态为一个二元组`(binary_path, current_node)`，其中第一个元素表示当前的节点访问状态，第二个元素表示当前访问到了哪个节点。结合双向队列`deque`，我们首先初始化，往队列中添加初始状态`(1 << x, x) for x in range(n)`，实际上列举了从所有节点开始访问路径的情况
3. 初始化二维数组`dist`，其中的元素`dist[i][j]`实际上表示了对于访问路径十进制值`i`，当访问到节点`j`时，此时当前路径的距离总长度。对于初始化情况，我们需要将`dist[1 << i][i]`全部置为0
4. 利用广度优先搜索算法`BFS`，我们取当前队列的头元素`(state, cur)`，判断当前的路径状态是否访问完了所有节点，若是则直接返回当前状态对应的路径长度；反之，则需要取当前节点`cur`的所有邻居节点，并进行访问，更新当前路径状态`state_new = state | (1 << neighbor)`，并且访问该节点的最短路径综合，将新的访问状态`(state_new, neighbor)`添加进队列的尾部继续遍历
5. 最终，如果访问完所有状态，都没有得到最短访问全部节点的路径长度，直接返回`-1`



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework11/figures/2.jpg)

