# 06 - 条件判断

## 📌 本节知识点

这一节主要学习 Python 中的条件判断，包括：

- 条件判断的基本作用
- `if` 单分支判断
- `if-else` 双分支判断
- `if-elif-else` 多分支判断
- `elif` 和 `else` 的使用规则
- 条件判断的执行顺序
- Python 中的缩进和代码块
- 条件表达式
- Python 中的真假值
- `and`、`or`、`not` 逻辑运算符
- 链式比较
- `input()` 获取用户输入
- `int()` 将字符串转换为整数
- 三元表达式

---

# 1. 条件判断

程序有时需要根据不同的条件执行不同的代码。

例如：

```text
年龄 >= 18
    ↓
输出 adult

年龄 < 18
    ↓
输出 teenager
```

这种根据条件选择不同执行路径的结构就是：

```text
条件判断
```

Python 中主要使用：

```python
if
elif
else
```

实现条件判断。

基本执行过程可以理解为：

```text
判断条件
   ↓
条件是否成立？
   │
 ┌─┴─┐
是   否
↓     ↓
执行   跳过
代码   代码
```

---

# 2. `if` 单分支判断

最基本的条件判断使用：

```python
if
```

基本格式：

```python
if 条件:
    条件成立时执行的代码
```

例如：

```python
age = 20

if age >= 18:
    print("你已经成年了")
    print("可以去网吧了")
```

因为：

```text
age = 20
```

所以：

```text
age >= 18
```

结果为：

```text
True
```

因此执行 `if` 中的代码：

```text
你已经成年了
可以去网吧了
```

---

# 3. `if` 的执行过程

例如：

```python
age = 20

if age >= 18:
    print("adult")
```

整个过程可以理解为：

```text
age = 20
   ↓
age >= 18
   ↓
  True
   ↓
执行 print("adult")
```

如果：

```python
age = 15
```

那么：

```text
age >= 18
   ↓
  False
   ↓
跳过 if 中的代码
```

因此：

```text
if 后面的条件为 True
→ 执行对应代码块

if 后面的条件为 False
→ 跳过对应代码块
```

---

# 4. 条件后面的冒号 `:`

Python 的条件判断中：

```python
if age >= 18:
```

最后的：

```text
:
```

不能省略。

正确：

```python
if age >= 18:
    print("adult")
```

错误：

```python
if age >= 18
    print("adult")
```

缺少冒号会产生语法错误：

```text
SyntaxError
```

因此基本结构一定是：

```text
if 条件:
       ↑
      冒号
```

---

# 5. Python 使用缩进表示代码块

Python 不使用大括号 `{}` 表示代码块，而是使用：

```text
缩进
```

例如：

```python
if age >= 18:
    print("你已经成年了")
    print("可以去网吧了")
```

这里两个 `print()` 具有相同的缩进：

```text
if age >= 18:
│
├── print("你已经成年了")
│
└── print("可以去网吧了")
```

因此它们都属于：

```text
if 代码块
```

---

# 6. 缩进是 Python 语法的一部分

Python 中缩进不只是为了让代码看起来整齐，而是会直接影响程序结构。

例如：

```python
if age >= 18:
    print("adult")

print("程序结束")
```

这里：

```python
print("adult")
```

属于 `if`。

但是：

```python
print("程序结束")
```

已经退出缩进，因此不属于 `if`。

可以理解为：

```text
if age >= 18:
    │
    └── print("adult")    ← 属于 if

print("程序结束")         ← 不属于 if
```

通常统一使用：

```text
4 个空格
```

作为一级缩进。

同一个代码块中的缩进应该保持一致。

---

# 7. `if-else` 双分支判断

如果需要在条件成立和不成立时分别执行不同代码，可以使用：

```python
if-else
```

基本格式：

```python
if 条件:
    条件成立时执行
else:
    条件不成立时执行
```

例如：

```python
age = 20

if age >= 18:
    print("adult")
else:
    print("teenager")
```

因为：

```text
20 >= 18
```

结果为：

```text
True
```

所以输出：

```text
adult
```

---

# 8. `if-else` 的执行过程

整个结构可以表示为：

```text
             age >= 18
                 │
          ┌──────┴──────┐
          │             │
        True          False
          │             │
          ↓             ↓
      "adult"       "teenager"
```

因此：

```text
if 条件成立
→ 执行 if

if 条件不成立
→ 执行 else
```

`if-else` 两个分支中只会执行其中一个。

---

# 9. `if-elif-else` 多条件判断

如果存在多个条件，可以使用：

```python
if
elif
else
```

例如：

```python
age = 20

if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
```

这里有三个可能的结果：

```text
age >= 18
→ adult

age < 18 并且 age >= 6
→ teenager

前面的条件都不满足
→ kid
```

---

# 10. 多分支判断的执行顺序

`if-elif-else` 会按照：

```text
从上到下
```

依次判断。

例如：

```python
if age >= 18:
    print("adult")

elif age >= 6:
    print("teenager")

else:
    print("kid")
```

执行过程：

```text
        age >= 18 ?
             │
       ┌─────┴─────┐
      True        False
       │             │
    adult        age >= 6 ?
                    │
              ┌─────┴─────┐
             True        False
              │             │
          teenager         kid
```

---

# 11. 命中一个分支后停止判断

`if-elif-else` 中：

```text
只会执行第一个满足条件的分支
```

例如：

```python
age = 20

if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
```

`20` 同时满足：

```text
20 >= 18
20 >= 6
```

但是程序首先判断：

```text
age >= 18
```

结果已经是：

```text
True
```

所以执行：

```text
adult
```

然后整个条件结构结束。

不会继续判断：

```python
elif age >= 6:
```

因此：

```text
从上往下判断
      ↓
找到第一个 True
      ↓
执行对应分支
      ↓
结束整个条件结构
```

---

# 12. 条件顺序很重要

因为程序会执行第一个满足条件的分支，所以条件顺序会影响最终结果。

例如：

```python
age = 20

if age >= 6:
    print("teenager")
elif age >= 18:
    print("adult")
```

因为：

```text
20 >= 6
```

已经成立，所以直接输出：

```text
teenager
```

后面的：

```python
age >= 18
```

不会继续判断。

因此对于这种具有范围包含关系的条件，通常应该：

```text
先判断范围更严格的条件
再判断范围更宽的条件
```

例如：

```python
if age >= 18:
    ...
elif age >= 6:
    ...
```

---

# 13. `elif` 和 `else`

`elif` 可以有多个。

例如：

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

因此：

```text
elif → 可以有多个
```

而：

```text
else → 最多一个
```

并且 `else` 应该放在整个条件结构的最后。

可以记成：

```text
if
 ↓
elif
 ↓
elif
 ↓
elif
 ↓
else
```

---

# 14. 条件表达式

`if` 后面的内容称为：

```text
条件表达式
```

例如：

```python
age >= 18
```

就是一个条件表达式。

比较运算通常会得到：

```text
True
```

或者：

```text
False
```

例如：

```python
print(20 >= 18)
```

结果：

```text
True
```

而：

```python
print(10 >= 18)
```

结果：

```text
False
```

因此：

```text
条件表达式
    ↓
True / False
    ↓
决定是否执行对应代码
```

---

# 15. Python 中的真假值

Python 的 `if` 后面不一定必须直接写：

```python
True
```

或者：

```python
False
```

其他对象也可以参与真假判断。

例如：

```python
if "hello":
    print("非空字符串是 True")
```

输出：

```text
非空字符串是 True
```

因为：

```text
"hello"
```

是非空字符串，在条件判断中会被视为：

```text
True
```

---

# 16. 常见的 False 值

常见的假值包括：

| 值 | 含义 |
| --- | --- |
| `False` | 布尔假值 |
| `0` | 整数零 |
| `0.0` | 浮点数零 |
| `""` | 空字符串 |
| `[]` | 空列表 |
| `{}` | 空字典 |
| `None` | 空值 |

例如：

```python
if 0:
    print("这行不会执行")
else:
    print("0 是 False")
```

输出：

```text
0 是 False
```

---

# 17. 常见的 True 值

与假值相对，常见的真值包括：

```text
非零数字
非空字符串
非空列表
非空字典
其他非空对象
```

例如：

```python
if 10:
    print("True")

if "hello":
    print("True")

if [1, 2, 3]:
    print("True")
```

这些条件都会被视为真。

可以先简单记成：

```text
0、空值、None
      ↓
    False


非零、非空
      ↓
     True
```

---

# 18. 利用真假值判断容器是否为空

因为空列表会被视为：

```text
False
```

所以可以直接写：

```python
my_list = [1, 2, 3]

if my_list:
    print("列表不为空")
```

而不一定需要写：

```python
if len(my_list) > 0:
    print("列表不为空")
```

两种方式都能表达相应判断，但直接使用：

```python
if my_list:
```

更加简洁。

---

# 19. 逻辑运算符

当一个条件中需要组合多个判断时，可以使用逻辑运算符。

Python 中主要有：

```text
and
or
not
```

对应：

| 运算符 | 含义 |
| --- | --- |
| `and` | 且 |
| `or` | 或 |
| `not` | 非 / 取反 |

---

# 20. `and`：且

`and` 表示：

```text
两个条件都成立，整体才成立
```

例如：

```python
x = 15

if x > 10 and x < 20:
    print(f"{x} 在 10 到 20 之间")
```

这里：

```text
x > 10
```

结果：

```text
True
```

同时：

```text
x < 20
```

结果：

```text
True
```

因此：

```text
True and True
```

结果：

```text
True
```

最终输出：

```text
15 在 10 到 20 之间
```

---

# 21. `and` 的判断规则

可以整理为：

| 条件 A | 条件 B | `A and B` |
| --- | --- | --- |
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

因此：

```text
and
 ↓
全部为 True
 ↓
结果才是 True
```

---

# 22. `or`：或

`or` 表示：

```text
只要有一个条件成立，整体就成立
```

例如：

```python
age = 70

if age < 6 or age >= 60:
    print("满足条件")
```

这里：

```text
age < 6
```

结果为：

```text
False
```

但是：

```text
age >= 60
```

结果为：

```text
True
```

因此：

```text
False or True
```

最终结果：

```text
True
```

---

# 23. `or` 的判断规则

| 条件 A | 条件 B | `A or B` |
| --- | --- | --- |
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

因此：

```text
or
 ↓
至少一个 True
 ↓
结果就是 True
```

---

# 24. `not`：取反

`not` 用于将真假结果反转。

例如：

```python
x = 15

if not x > 100:
    print(f"{x} 不大于 100")
```

首先：

```text
x > 100
```

结果：

```text
False
```

然后：

```text
not False
```

结果：

```text
True
```

所以执行：

```text
15 不大于 100
```

---

# 25. `not` 的判断规则

规则比较简单：

```text
not True
    ↓
  False


not False
    ↓
   True
```

也就是：

```text
not → 真假取反
```

---

# 26. 三种逻辑运算符总结

可以统一记成：

```text
and
↓
并且
↓
全部成立才成立


or
↓
或者
↓
至少一个成立就成立


not
↓
取反
↓
True ↔ False
```

---

# 27. 链式比较

Python 支持链式比较。

例如：

```python
x = 15

if 10 < x < 20:
    print("x 在 10 到 20 之间")
```

这里：

```python
10 < x < 20
```

可以理解为：

```python
x > 10 and x < 20
```

当：

```text
x = 15
```

时：

```text
10 < 15 < 20
```

成立。

因此执行对应代码。

---

# 28. 链式比较与 `and`

下面两种写法表达的条件相同：

```python
if x > 10 and x < 20:
    print(x)
```

以及：

```python
if 10 < x < 20:
    print(x)
```

可以建立关系：

```text
x > 10 and x < 20
          ↓
     10 < x < 20
```

链式比较的形式和数学中的范围表达比较接近。

---

# 29. `input()` 获取用户输入

Python 可以使用：

```python
input()
```

获取用户输入。

例如：

```python
s = input("请输入你的年龄：")
```

程序运行后会等待用户输入内容。

例如输入：

```text
20
```

变量：

```python
s
```

中会保存用户输入的数据。

---

# 30. `input()` 返回字符串

`input()` 有一个非常重要的特点：

```text
input() 返回 str
```

即使输入：

```text
20
```

得到的也是：

```python
"20"
```

而不是整数：

```python
20
```

例如：

```python
s = input("请输入你的年龄：")

print(type(s))
```

如果输入：

```text
20
```

得到的类型仍然是：

```text
<class 'str'>
```

因此一定要区分：

```text
"20" → str

20   → int
```

---

# 31. `int()` 将输入转换为整数

如果用户输入的是年龄，并且后面需要进行数字比较，就需要先转换类型。

例如：

```python
s = input("请输入你的年龄：")

age = int(s)
```

整个过程：

```text
用户输入
   ↓
  "20"
   ↓
 input()
   ↓
  str
   ↓
 int()
   ↓
  20
   ↓
  int
```

之后才能正常进行：

```python
if age >= 18:
    print("adult")
```

---

# 32. 为什么需要转换输入类型

如果：

```python
s = input("请输入你的年龄：")
```

用户输入：

```text
20
```

此时：

```text
s = "20"
```

如果直接进行：

```python
s >= 18
```

实际上是在比较：

```text
str 和 int
```

这种比较会产生：

```text
TypeError
```

因此数字输入通常需要：

```python
age = int(input("请输入你的年龄："))
```

这样可以直接完成：

```text
input()
   ↓
获得字符串
   ↓
int()
   ↓
转换成整数
```

---

# 33. 三元表达式

对于比较简单的二选一赋值，可以使用条件表达式，也常被称为三元表达式。

基本格式：

```python
条件成立时的值 if 条件 else 条件不成立时的值
```

例如：

```python
age = 20

result = "adult" if age >= 18 else "kid"

print(result)
```

输出：

```text
adult
```

执行逻辑：

```text
          age >= 18
              │
       ┌──────┴──────┐
       │             │
     True          False
       │             │
       ↓             ↓
   "adult"         "kid"
```

最终把其中一个值赋给：

```text
result
```

---

# 34. 三元表达式与 `if-else`

例如：

```python
if age >= 18:
    result = "adult"
else:
    result = "kid"
```

可以简写为：

```python
result = "adult" if age >= 18 else "kid"
```

两种方式表达的逻辑相同。

普通写法：

```text
if condition:
    result = A
else:
    result = B
```

三元表达式：

```text
result = A if condition else B
```

三元表达式比较适合简单的条件赋值。

如果逻辑比较复杂，仍然使用普通的：

```python
if
elif
else
```

结构更加清晰。

---

# 35. 条件判断常见错误

## 忘记冒号

错误：

```python
if age >= 18
    print("adult")
```

正确：

```python
if age >= 18:
    print("adult")
```

---

## 缩进错误

同一个代码块应该保持相同缩进。

正确：

```python
if age >= 18:
    print("adult")
    print("成年")
```

通常统一使用：

```text
4 个空格
```

---

## 条件顺序错误

例如：

```python
if age >= 6:
    print("teenager")
elif age >= 18:
    print("adult")
```

对于：

```text
age = 20
```

第一个条件已经成立，所以不会继续判断第二个条件。

应该根据范围关系合理安排判断顺序。

---

## 忘记转换 `input()` 的结果

```python
age = input("请输入年龄：")
```

此时：

```text
age → str
```

如果需要数字比较，可以：

```python
age = int(input("请输入年龄："))
```

转换为：

```text
int
```

---

# 🧠 本节重点总结

## `if`

基本格式：

```python
if 条件:
    代码
```

执行逻辑：

```text
条件
 ↓
True
 ↓
执行代码
```

如果条件为：

```text
False
```

则跳过对应代码块。

---

## `if-else`

基本格式：

```python
if 条件:
    条件成立时执行
else:
    条件不成立时执行
```

关系：

```text
        condition
            │
      ┌─────┴─────┐
     True        False
      │             │
      ↓             ↓
     if            else
```

---

## `if-elif-else`

基本格式：

```python
if 条件1:
    ...
elif 条件2:
    ...
elif 条件3:
    ...
else:
    ...
```

执行顺序：

```text
从上往下判断
      ↓
遇到第一个 True
      ↓
执行对应分支
      ↓
结束判断
```

---

## 缩进

Python 使用：

```text
缩进
```

表示代码块。

例如：

```python
if age >= 18:
    print("adult")
    print("成年")
```

两个 `print()` 都属于 `if`。

通常：

```text
一级缩进 → 4 个空格
```

---

## 真假值

常见 False：

```text
False
0
0.0
""
[]
{}
None
```

常见 True：

```text
非零数字
非空字符串
非空列表
非空字典
其他非空对象
```

可以先简单记成：

```text
零 / 空 / None → False

非零 / 非空    → True
```

---

## `and`

```text
A and B
```

表示：

```text
A 和 B 都成立
```

只有：

```text
True and True
```

结果才是：

```text
True
```

---

## `or`

```text
A or B
```

表示：

```text
A 或 B 至少一个成立
```

只有：

```text
False or False
```

结果才是：

```text
False
```

---

## `not`

```text
not True  → False

not False → True
```

表示：

```text
取反
```

---

## 链式比较

```python
10 < x < 20
```

可以理解为：

```python
x > 10 and x < 20
```

---

## `input()`

```python
s = input("请输入：")
```

得到：

```text
str
```

即使输入数字：

```text
20
```

得到的仍然是：

```text
"20"
```

---

## `int()` 转换输入

```python
age = int(input("请输入年龄："))
```

转换过程：

```text
用户输入
   ↓
  str
   ↓
 int()
   ↓
  int
```

---

## 三元表达式

普通写法：

```python
if age >= 18:
    result = "adult"
else:
    result = "kid"
```

可以写成：

```python
result = "adult" if age >= 18 else "kid"
```

基本结构：

```text
成立时的值 if 条件 else 不成立时的值
```

---

# 🔗 条件判断整体关系

这一部分可以统一整理成：

```text
                        条件判断
                           │
           ┌───────────────┼───────────────┐
           │               │               │
          if            if-else      if-elif-else
           │               │               │
         单分支           双分支           多分支
           │               │               │
           └───────────────┼───────────────┘
                           │
                           ↓
                       条件表达式
                           │
                   ┌───────┴───────┐
                   │               │
                 True            False
                   │               │
                   └───────┬───────┘
                           │
                           ↓
                       选择分支
```

多个条件可以通过：

```text
and / or / not
```

进行组合：

```text
and → 并且

or  → 或者

not → 取反
```

用户输入参与条件判断时：

```text
input()
   ↓
  str
   ↓
需要数字比较
   ↓
 int()
   ↓
  int
   ↓
if 条件判断
```

---

# ✅ 本节掌握

完成这一部分后，需要能够理解和使用：

- 理解条件判断的作用
- 使用 `if` 进行单条件判断
- 使用 `if-else` 进行双分支判断
- 使用 `if-elif-else` 进行多分支判断
- 理解 `elif` 可以出现多个
- 理解 `else` 最多一个并位于最后
- 理解多分支判断从上往下执行
- 理解命中第一个满足条件的分支后不会继续判断
- 能够合理安排多个条件的判断顺序
- 知道条件后需要使用冒号 `:`
- 理解 Python 使用缩进表示代码块
- 知道同一代码块应该保持一致缩进
- 理解条件表达式最终参与真假判断
- 掌握常见的 True 和 False 值
- 知道 `0`、空字符串、空列表、空字典和 `None` 等会被视为 False
- 知道非零数字和非空容器通常会被视为 True
- 使用 `and` 组合多个必须同时成立的条件
- 使用 `or` 表示至少一个条件成立
- 使用 `not` 对真假结果取反
- 使用 `10 < x < 20` 这样的链式比较
- 理解链式比较与 `and` 组合比较的关系
- 使用 `input()` 获取用户输入
- 理解 `input()` 返回的是字符串 `str`
- 使用 `int()` 将数字字符串转换成整数
- 避免直接比较 `str` 和 `int`
- 能够使用简单的三元表达式
- 理解三元表达式与普通 `if-else` 的对应关系