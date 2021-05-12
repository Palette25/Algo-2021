## 算法分析与复杂性理论 - Homework 8

#### 姓名：陈明亮

#### 学号：2001212817



### LeetCode 235.  二叉搜索树的最近公共祖先

#### 题目：

> 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
>
> 百度百科中最近公共祖先的定义为：
>
> “对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



#### 代码：

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root
```



#### 算法思路描述：(时间复杂度O(n)，空间复杂度O(1))

1. 采用递归的方式进行最近公共祖先节点的查找，已知输入为二叉搜索树`BST`，存在以下性质：

   * 左子节点的值小于根节点的值
   * 右子节点的值大于根节点的值

2. 递归判断目标节点`p`和`q`的值与当前的根节点`root`的值大小关系，根据`BST`二叉搜索树的性质：

   * 当`p`和`q`的值都大于`root`的值时，最近公共祖先节点必定在当前`root`节点的右子树中，递归访问`root.right`

   * 当`p`和`q`的值都小于`root`的值时，最近公共祖先节点必定在当前`root`节点的左子树中，递归访问`root.left`

   * 不满足上述两个条件时，那么存在以下三种情况：

     1. 当前根节点`root`恰好为`p`节点，`q`节点在其子树中，那么最近公共祖先就是`p`节点，即当前的`root`节点
     2. 当前根节点`root`恰好为`q`节点，`p`节点在其子树中，那么最近公共祖先就是`q`节点，即当前的`root`节点
     3. `p`和`q`分别在`root`节点的左右子树中，那么最近公共祖先就是`root`节点

     所以，以上情况均返回`root`节点本身作为结果即可



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework8/figures/1.jpg)



### LeetCode 110.  平衡二叉树

#### 题目：

> 给定一个二叉树，判断它是否是高度平衡的二叉树。
>
> 本题中，一棵高度平衡二叉树定义为：
>
> ​	一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1 。



#### 代码：

```python
class Solution:
    def getHeight(self, root: TreeNode) -> int:
        # Empty Node
        if not root: 
            return 0
        # Leaf Node
        if root.left == None and root.right == None:
            return 1

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        # Empty Node
        if not root: 
            return True
        # Leaf Node
        if root.left == None and root.right == None:
            return True
        # First check children's balance
        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        if not leftBalanced or not rightBalanced:
            return False
        
        # Then check root node's balance
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return True
```



#### 算法思路描述：（时间复杂度O(n)，空间复杂度O(1)）

1. 采用自底向上的递归方法，首先判断当前节点的左子树和右子树是否都为平衡二叉树，若都是的话才进一步判断当前树是否平衡，反之则返回`False`，即当前树不平衡
2. 判断当前树是否平衡，需要判断当前左右子树的高度差是否超过一，首先需要编写高度函数`getHeight()`，该函数也通过递归的方式，分别获取当前左右子树的高度，取其最大值加一作为当前树的高度。然后通过判断当前左右子树的高度差是否超过1，即可得到当前树是否平衡



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework8/figures/2.jpg)



### LeetCode 257 . 二叉树的所有路径

#### 题目：

> 给定一个二叉树，返回所有从根节点到叶子节点的路径。
>
> **说明:** 叶子节点是指没有子节点的节点。



#### 代码：

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs_path(root: TreeNode, path: str):
            if root:
                path += str(root.val)
                # Judge if is the leaf node
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += '->'
                    # Recursion
                    dfs_path(root.left, path)
                    dfs_path(root.right, path)

        res = []
        dfs_path(root, '')
        
        return res
```



#### 算法思路描述：（时间复杂度O(n ^ 2)，空间复杂度O(n)）

1. 采取递归方式的深度优先搜索算法`DFS`进行解决，首先需要定义结果数组`res`存储返回的路径字符串，然后调用深度优先搜索函数`dfs_path`，包含两个参数：`root` - 表示当前递归到的根节点, `path` - 递归到该节点之前的路径字符串
2. 深度优先搜索函数中，首先判断当前`root`是否为空，若是的话则直接`return`，反之则将传入的路径字符串`path`进行拷贝然后添加当前节点的值。如果当前节点没有左右子树，即为叶子节点，则将`path`添加到结果数组中；反之则为路径字符串`path`加上`->`，同时递归地访问当前节点的左右子节点



#### 结果截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework8/figures/3.jpg)

