## 算法分析与复杂性理论 - Homework 3

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 16. 最接近的三数之和

#### 题目：

> 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
>
> 返回这三个数的和。
>
> 假定每组输入只存在唯一答案。

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework3/figures/1.jpg)

#### 代码：

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dis, res = 2 * 10 ** 4 + 1, 0  # Set max number, making biggest distance
        size = len(nums)
        nums.sort()

        for index, ele in enumerate(nums):
            # Use double pointers to find triplet making smallest distance
            left, right = index+1, size-1
            while left < right:
                new_sum = ele + nums[left] + nums[right]
                # If equal, directly return
                if new_sum == target:
                    return target
                # Else get pos/neg flag
                flag = True if new_sum > target else False
                new_dis = abs(new_sum - target)
                if new_dis < dis:
                    dis, res = new_dis, new_sum
                # Move pointers twords zero distance
                if flag:
                    right -= 1
                else:
                    left += 1

        return res
```

#### 算法思路描述：(时间复杂度O(n^2)，空间复杂度O(1))

1. 该题与*3Sum*非常相似，不同之处就在于需要找到的是与*target*数值最接近的三数之和

2. 本题的话也可以采用三指针的方式进行求解：

   - 首先设定一个非常大的距离变量*dis*，用他来存储当前三数与*target*之间的差值；结果变量*res*用于存储最接近的三数的和

   - 首先需要借助*sort*函数将数组*nums*进行升序排序

   - 然后通过一个*for*循环从左到右遍历当前数组*nums*，当前访问到的下标位置为*index*，在循环体内我们构造双指针*left*和*right*，并且分别初始化为：*left=index+1*, *right=size-1*，即左指针是当前下标加1，右指针是数组最大下标

   - 设定*while*循环，循环条件为*left < right*，在此循环体内我们每次都计算当前三个下标指针*index, left, right*对应的三个元素之和*sum*，并且计算*sum*与*target*之间的距离绝对值，若距离小于当前的*dis*，则更新当前最小距离与最接近的三数之和

   - 然后根据当前三元素之和*sum*与*target*的大小关系，决定左右指针的更新：如果*sum < target*，那么左指针向右移动一位；反之右指针向左移动一位

     

### LeetCode 17. 电话号码的数字组合

#### 题目：

> 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
>
> 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
>

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework3/figures/0.png)

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework3/figures/2.jpg)

#### 代码：

```python
class Solution:
    def __init__(self):
        self.res = []
        self.letters = [
            'abc', 'def', 'ghi', 'jkl', 
            'mno', 'pqrs', 'tuv', 'wxyz'
        ]
        self.digits = None

    def getCombination(self, index: int, sstr: str):
        # Recurrence end condition
        if index == len(self.digits):
            self.res.append(sstr)
            return
        
        char = int(self.digits[index])
        string = self.letters[char - 2]

        for ele in string:
            self.getCombination(index+1, sstr + ele)

    def letterCombinations(self, digits: str) -> List[str]:
        # Violent sloving method
        if len(digits) == 0:
            return []
        self.digits = digits
        self.getCombination(0, "")

        return self.res
```

#### 算法思路描述：（时间复杂度O(3^m * 4^n)，空间复杂度O(1)）

1. 本题的时间复杂度为*O(3^m x 4^n)*，其中m为输入的数字中对应三个字母的数字个数，n为对应四个字母的数字个数
2. 可以采用递归的思想求解该题，即使用递归函数逐步列举出所有对应存在的字母组合字符串
3. 首先，修改当前类*Solution*的初始化函数，添加*res*数组存储所有的字母组合串，*letters*数组对应每个数字能够表示的字母串，*digits*数组存储输入的数字串。之所以添加这些变量，是为了减少递归函数参数传递中的冗余操作
4. *getCombination*是核心递归函数，接收参数*index*表示当前访问到的数字下标，*sstr*表示当前已构造出的字母串
5. 递归函数内部首先需要设置递归终止条件：当访问到的数字下标等于*digits*的大小时，将当前构造完成的字母串*sstr*放进结果数组*res*中，终止递归；反之，当递归没有到达终止时，根据当前访问的数字元素，获取其在*letters*数组中对应的可表示字母，然后建立*for*循环，对于每个可表示的字母*ele*，循环体内再次调用递归函数，传递的参数为*index+1*，与当前已构造字符串*sstr*加上*ele*，继续递归操作，最后的结果能获取到所有的字母组合结果



### LeetCode 19. 删除链表的倒数第N个节点

#### 题目：

> 给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。
>
> **进阶：**你能尝试使用一趟扫描实现吗？

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework3/figures/3.jpg)

#### 代码：

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre, cur, tail = head, head, head
        # Let tail node move n-1 steps firstly
        for i in range(n-1):
            tail = tail.next
        # Then move three pointers until tail.next.next is None
        while tail.next:
            if tail.next.next: 
                # pre move one step less than cur
                pre, cur, tail = pre.next, cur.next, tail.next
            else:
                cur, tail = cur.next, tail.next
        # Judge if to delete head
        if cur == head:
            return head.next        
        # cur node is the node to delete
        pre.next = cur.next

        return head
```

#### 算法思路描述：（时间复杂度O(n)，空间复杂度O(1)）

1. 只用一遍顺序扫描就实现链表倒数第N个节点的删除，需要同时存储三个指针*pre, cur, tail*，这三个指针分别代表：目标结点的前一个结点，目标结点，链表尾结点，三个指针初始化值都为*head*头节点

2. 那么，为了正确访问到链表倒数第N个结点，需要先让尾结点*tail*先走N-1步，然后让*tail*和*cur*和*pre*一起顺序扫描，构建*while*循环，循环条件为*tail.next != None*，在循环体内判断尾节点*tail*的下下个结点是否为*None*，是的话则只更新*cur*和*tail*结点，反之则更新全部的结点为当前结点的*next*，目的是为了让*pre*指针比*cur*指针少走一步

3. 最后，首先判断需要删除的结点*cur*是否为头节点，是的话直接返回*head.next*即可，反之则更新*pre*的*next*为*cur*结点的*next*，达到删除*cur*结点的目的，最后返回头节点

   

