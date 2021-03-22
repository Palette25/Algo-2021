## 算法分析与复杂性理论 - Homework 2

#### 姓名：陈明亮

#### 学号：2001212817

### LeetCode 7. 整数反转

#### 题目：

> 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
>
> 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
>
> 假设环境不允许存储 64 位整数（有符号或无符号）。
>

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework2/figures/1.jpg)

#### 代码：

```python
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        while x :
            pop = x % 10 if x > 0 else x % (-10)
            x = x // 10 if x > 0  else int(x/10)
            
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
            if res < int(INT_MIN / 10) or (res == int(INT_MIN / 10) and pop < INT_MIN % -10):
                return 0
            res = res * 10 + pop
        
        return res
```

#### 算法思路描述：(时间复杂度O(n)，空间复杂度O(1))

1. 首先手动计算32位有符号整数*int*类型的取值上界*INT_MAX*和下界*INT_MIN*，因为在*python*语言里边的话没法直接获取某数值类型的取值范围

2. 构建一个*while*循环，循环条件为*x!=0*，设定结果为*res*，然后结合栈*Stack*先进后出的思想，每次取输入整数*x*的最后一位数字 -- 类似于*pop*操作，并将该位数字*push*进结果*res*的末尾位置。此处不需要借助真实的栈数据结构，通过对*x*除10取模操作实现*pop*，对*res*乘10加模实现*push*操作。

3. 但是，在*python*中，对负数进行取模必须除以对应的基数加上负号，对负数进行整除时需改为*int(x/10)*

4. 为了防止反转后的整数超过32位有符号整数的取值范围，在循环内部需要检测当前的计算结果*res*是否超出了*[INT_MIN, INT_MAX]*，如果超出该范围的话则直接返回0

   

### LeetCode 66. 加一

#### 题目：

> 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
>
> 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
>
> 你可以假设除了整数 0 之外，这个整数不会以零开头。
>

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework2/figures/2.jpg)

#### 代码：

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        l = len(digits)

        for i in range(l):
            tmp = (digits[l-1-i] + carry) // 10
            digits[l-1-i] = (digits[l-1-i] + carry) % 10
            carry = tmp

            if carry == 0:
                break
        
        # Judge if need to create new element
        if carry >= 1:
            digits.insert(0, carry)

        return digits
```

#### 算法思路描述：（时间复杂度O(n)，空间复杂度O(1)）

1. 设定进位数字*carry=1*，设定*for*循环，在循环内从后向前遍历当前数组*digits*，如果当前的进位不为0的话，将当前数字加上进位，整除以10产生新的进位*carry*，模10结果赋给当前数组元素；如果当前进位为0的话，直接跳出循环
2. 最后，检测当前进位是否为0，是则返回当前数组，反之则在*digits*的头部插入*carry*，产生进位后的新数组元素



### LeetCode 13. 罗马数字转整数

#### 题目：

> 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
>
> 字符          数值
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000
> 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
>
> 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
>
> I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
> X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
> C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
> 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

#### 测试截图：

![img](https://github.com/Palette25/Algo-2021/blob/main/Homework2/figures/3.jpg)

#### 代码：

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        res, index = 0, len(s)-1
        dd = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # Poping stack and analyse by rules
        while index >= 0:
            a = s[index]
            if index - 1 < 0: 
                res += dd[a]
            else :
                b = s[index-1]
                if dd[b] >= dd[a]:
                    res += dd[a]
                else:
                    index -= 1
                    res += dd[a] - dd[b]
            index -= 1
        
        return res
```

#### 算法思路描述：（时间复杂度O(n)，空间复杂度O(k)）

1. 此题也需要结合栈先进后出的思想，首先构建字典类型*d*，将罗马数字中的字符对应到他们原本的数值上

2. 然后构建*while*循环，设*index*为当前访问的字符下标，初始值为*str*的最后一个元素下标，通过从后向前访问*str*，来模拟栈的各项操作：

   * 每次取出*a = s[index]*作为*pop*操作
   * 判断当前*index*是否小于0，判断当前的‘栈’是否为空
   * 将*index+=1*撤销上一次pop操作

3. 循环体内的步骤为：

   * 每次取出当前‘栈顶’，即*a=s[index]*，同时判断取出后‘栈’是否为空，若是的话直接为最终返回值*res*加上*d[a]*，反之则继续取出当前‘栈顶’*b*
   * 已知罗马数字中一般情况下左边的数字要大于或者等于右边的数字，如果符合该条件，则将上一次*pop*操作撤销，将当前*d[a]*加入返回值；反之则触发特殊规则，将返回值加上*d[a]-d[b]*

   

