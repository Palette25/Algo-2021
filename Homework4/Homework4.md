## 算法分析与复杂性理论 - Homework 4

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 56. 合并区间

#### 题目：

> 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
>
> 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework4/figures/1.jpg)

#### 代码：

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort all the intervals with key as left-bounding (ascending order)
        intervals.sort(key=lambda x : x[0])

        result = []
        # Push first interval into result
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            # Judge whether current interval's left-bounding is larger
            # than result's last interval's right-bounding
            # If yes, no overlap
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            # If no, merge them
            else:
                result[-1][1] = max(intervals[i][1], result[-1][1])

        return result
```

#### 算法思路描述：(时间复杂度O(nlogn)，空间复杂度O(n))

1. 首先将*intervals*内部的每个子区间*interval*，按照其起始位置的大小，从小到大进行升序排序。此处结合*lambda*表达式，将*sort*函数的*key*修改为每个子区间列表的第一个元素，完成排序过程
2. 排序完成之后，先将第一个元素*append*进结果区间数组*result*中，然后进行顺序遍历，对于遍历到的每个子区间，如果其起始位置比当前结果区间数组*result*的最后一个区间的终止位置大，那么不存在重叠，直接将该子区间添加到结果数组中；反之则存在重叠，将当前结果区间数组中的最后一个子区间的终止位置，更改为当前遍历到的这个区间的终止位置与其两者之间的最大值



### LeetCode 148. 排序链表

#### 题目：

> 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
>
> 进阶：你可以在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
>

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework4/figures/2.jpg)

#### 代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Function to merge two node lists
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            t0, t1, t2 = dummyHead, head1, head2
            while t1 and t2:
                if t1.val <= t2.val:
                    t0.next = t1
                    t1 = t1.next
                else:
                    t0.next = t2
                    t2 = t2.next
                t0 = t0.next
            if t1:
                t0.next = t1
            elif t2:
                t0.next = t2
            return dummyHead.next

        if head == None:
            return head
        
        dummyHead, tmp = ListNode(0, head), head

        # Sequential Traversal to get node list's length
        length = 0
        while tmp:
            tmp = tmp.next
            length = length + 1
        
        # Here we use half-split methods to perform merge sorting for node list
        subLength = 1 # current split sub-list's length
        
        while subLength < length:
            prev, ptr = dummyHead, dummyHead.next
            while ptr:
                # Get first split of sub-list, length as subLength
                head1 = ptr
                for i in range(1, subLength):
                    if ptr and ptr.next: ptr = ptr.next
                    else: break
                
                # Unlink the first splited sub-list
                head2 = ptr.next
                ptr.next = None
                ptr = head2
                # Get second split of sub-list, length as subLength
                for i in range(1, subLength):
                    if ptr and ptr.next: ptr = ptr.next
                    else: break
                
                # Unlink the second splited sub-list, and record the next node
                forward = None
                if ptr:
                    forward = ptr.next
                    ptr.next = None
                # Merge that two sub-list
                merged = merge(head1, head2)
                # Link the merge result list to prev node
                prev.next = merged
                # Update prev node
                while prev.next:
                    prev = prev.next
                # Update ptr node,
                ptr = forward
            # Update sub-list length, towards next iteration of merging 
            subLength = subLength * 2

        return dummyHead.next
```

#### 算法思路描述：（时间复杂度O(nlogn)，空间复杂度O(1)）

1. 为了达到时间复杂度为*O(nlogn)*，空间复杂度为*O(1)*的目标，此处需要采用：基于二分归并排序的非递归做法，使得时间复杂度收缩到归并排序产生的*O(nlogn)*，同时避免递归操作调用的在栈空间上产生的空间复杂度*O(logn)*
2. 基于二分归并排序的非递归算法进行链表结构的排序主要分为以下几步：
   * 首先，采用顺序遍历获得链表的整体长度*length*，并且判断当前输入的头节点*head*是否为空，是的话则直接返回*head*，反之则继续执行
   * 然后，定义当前子链表的长度*subLength*，初始值为1；初始化*dummyHead*结点，并且将其*next*指向当前的头节点
   * 之后则进入到核心的归并排序过程，非递归做法设定两重*while*循环，第一重循环的条件为*subLength < length*，即当前分裂得到的子链表的长度不能大于原始链表的总长度，并且该重循环下进行的是长度为*subLength*的所有子链表的分裂-合并操作，设定*prev*变量作为当前已排序完成的链表尾节点，*ptr*作为当前访问到的结点，每次循环完成之后，都将*subLength*乘以2
   * 第二重循环的条件为*ptr != None*，该重循环下进行的是在当前链表中划分出两个长度为*subLength*的子链表，并且将两者合并的操作。首先分别进行两次*for*循环，得到两个分裂后的子链表的头节点*head1*,*head2*，对两个子链表进行合并操作，并且将合并结果链表接回到*prev*结点之后，进行下一轮操作
   * 链表的合并操作与数组的类似，然后分别顺序对两个链表的元素进行顺序遍历，将数值小的结点添加到结果链表之后，直到其中某一个链表访问到*None*之后，将剩下的链表元素全部顺序接入到结果链表后，返回即可



### LeetCode 274. H指数

#### 题目：

> 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
>
> h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。
>
> 例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
>

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework4/figures/3.jpg)

#### 代码：

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = 0
        N = len(citations)
        # Sort the citations list
        citations.sort()
        # After sorting, 
        # Find max h number
        while i < N and citations[N - 1 - i] > i:
            i += 1

        return i
```

#### 算法思路描述：（时间复杂度O(nlogn)，空间复杂度O(1)）

1. 首先对引用数组*citations*进行降序排序，根据h指数的定义可知，我们顺序遍历排序之后的数组，当遍历到最大的下标*index*，且满足*citations[index] > index*条件时，当前数组的h指数即为*index+1*(因为下标是从0开始的)

2. 也可以通过升序排序，倒序扫描的方法完成，设定*while*循环，当满足*i<N*，N为数组总长度，并且*citations[N-1-i]>i*时，令*i+=1*，累加之后的结果*i*即为需要返回的h指数

   

