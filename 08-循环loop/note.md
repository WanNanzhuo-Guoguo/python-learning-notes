# 08 - 循环 Loop

## 📌 本节知识点

- `for...in` 循环
- 使用 `for` 遍历列表等可迭代对象
- `range()` 生成整数序列
- `range(start, stop, step)` 的使用
- `while` 条件循环
- `break` 提前结束循环
- `continue` 跳过当前循环
- `for...else` 结构
- `enumerate()` 同时获取索引和值
- Python 循环中的一些注意事项

---

# 1. 什么是循环

循环用于让一段代码按照一定规则**重复执行**。

例如一个列表中保存了多个名字：

```python
names = ['Michael', 'Bob', 'Tracy']
```

如果希望依次输出每个人的名字，可以使用循环，而不需要分别写：

```python
print(names[0])
print(names[1])
print(names[2])
```

Python 中常用的循环主要有两种：

```text
循环
├── for...in → 遍历可迭代对象
└── while    → 根据条件重复执行
```

---

# 2. for...in 循环

基本语法：

```python
for 变量 in 可迭代对象:
    循环执行的代码
```

例如：

```python
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(f"Hello, {name}!")
```

输出：

```text
Hello, Michael!
Hello, Bob!
Hello, Tracy!
```

执行过程可以理解为：

```text
names = ['Michael', 'Bob', 'Tracy']

第一次循环
name = 'Michael'
      ↓
print("Hello, Michael!")

第二次循环
name = 'Bob'
      ↓
print("Hello, Bob!")

第三次循环
name = 'Tracy'
      ↓
print("Hello, Tracy!")

      ↓
遍历结束
```

因此：

```python
for name in names:
```

并不是手动控制下标，而是**依次从 `names` 中取出元素并赋值给 `name`**。:chatgpt-content-reference{index="3"}

---

# 3. for 可以遍历什么

`for...in` 可以遍历各种**可迭代对象（Iterable）**。

常见的有：

```text
list
tuple
str
range
dict
...
```

例如遍历字符串：

```python
for char in "Python":
    print(char)
```

输出：

```text
P
y
t
h
o
n
```

也就是说，`for` 循环的核心可以理解为：

```text
从一个可迭代对象中
      ↓
依次取出一个元素
      ↓
执行循环体
      ↓
继续取下一个元素
      ↓
直到遍历结束
```

---

# 4. 使用 enumerate() 同时获取索引和值

普通 `for` 循环默认直接获得元素：

```python
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)
```

如果除了元素本身，还需要知道它的**索引位置**，可以使用：

```python
enumerate()
```

例如：

```python
names = ['Michael', 'Bob', 'Tracy']

for i, name in enumerate(names):
    print(f"{i}: {name}")
```

输出：

```text
0: Michael
1: Bob
2: Tracy
```

这里每次循环都会得到两个值：

```text
第一次 → i = 0，name = 'Michael'
第二次 → i = 1，name = 'Bob'
第三次 → i = 2，name = 'Tracy'
```

因此：

```python
for i, name in enumerate(names):
```

可以理解为：

```text
enumerate(names)
        ↓
(索引, 元素)
        ↓
分别赋值给 i 和 name
```

当既需要**位置**又需要**元素值**时，`enumerate()` 很方便。:chatgpt-content-reference{index="4"}

---

# 5. range() 生成整数序列

如果需要让循环按照一定的数字范围执行，可以使用：

```python
range()
```

常见形式有三种：

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

---

## 5.1 range(stop)

例如：

```python
for i in range(5):
    print(i, end=" ")
```

输出：

```text
0 1 2 3 4
```

也就是：

```python
range(5)
```

对应：

```text
0 1 2 3 4
```

默认从：

```text
0
```

开始。

但是**不会包含 5**。

---

# 6. range(start, stop)

例如：

```python
for i in range(1, 6):
    print(i, end=" ")
```

输出：

```text
1 2 3 4 5
```

因此：

```python
range(1, 6)
```

表示：

```text
从 1 开始
   ↓
一直生成到 6 之前
   ↓
1 2 3 4 5
```

---

# 7. range(start, stop, step)

第三个参数表示：

```text
step → 步长
```

例如：

```python
for i in range(0, 10, 2):
    print(i, end=" ")
```

输出：

```text
0 2 4 6 8
```

这里：

```text
start = 0
stop  = 10
step  = 2
```

所以：

```text
0 → 2 → 4 → 6 → 8
```

每次增加 `2`。:chatgpt-content-reference{index="5"}

---

# 8. range() 的左闭右开

`range()` 一个非常重要的特点是：

```text
包含 start
不包含 stop
```

也就是：

```text
[start, stop)
```

例如：

```python
range(1, 6)
```

得到：

```text
1 2 3 4 5
```

而不是：

```text
1 2 3 4 5 6
```

所以可以记成：

```text
range(start, stop, step)

start → 从哪里开始
stop  → 到哪里之前停止
step  → 每次变化多少
```

三种形式对比：

| 写法 | 结果 |
|---|---|
| `range(5)` | `0 1 2 3 4` |
| `range(1, 6)` | `1 2 3 4 5` |
| `range(0, 10, 2)` | `0 2 4 6 8` |

:chatgpt-content-reference{index="6"}

---

# 9. 使用 for + range() 进行累加

例如计算：

```text
1 + 2 + 3 + ... + 100
```

可以写成：

```python
total = 0

for i in range(1, 101):
    total += i

print(total)
```

输出：

```text
5050
```

这里：

```python
range(1, 101)
```

实际产生：

```text
1 ~ 100
```

因为 `101` 不包含在范围中。

执行过程：

```text
total = 0

i = 1 → total = 0 + 1
i = 2 → total = 1 + 2
i = 3 → total = 3 + 3
...
i = 100
      ↓
total = 5050
```

其中：

```python
total += i
```

等价于：

```python
total = total + i
```

:chatgpt-content-reference{index="7"}

---

# 10. while 循环

`while` 是**条件循环**。

基本语法：

```python
while 条件:
    循环体
```

只要条件为：

```python
True
```

循环就会继续执行。

例如：

```python
n = 10

while n > 0:
    print(n, end=" ")
    n -= 1
```

输出：

```text
10 9 8 7 6 5 4 3 2 1
```

执行过程：

```text
n = 10
  ↓
n > 0 ? → True
  ↓
输出 10
  ↓
n = 9
  ↓
n > 0 ? → True
  ↓
继续执行
  ↓
...
  ↓
n = 0
  ↓
n > 0 ? → False
  ↓
循环结束
```

:chatgpt-content-reference{index="8"}

---

# 11. for 和 while 的区别

两者都可以实现循环，但使用场景不同。

| 循环 | 特点 | 常见场景 |
|---|---|---|
| `for...in` | 依次遍历元素 | 遍历列表、字符串、range 等 |
| `while` | 根据条件决定是否继续 | 不确定具体循环次数时 |

例如：

```python
for i in range(10):
```

通常表示：

```text
已经知道需要遍历的范围
```

而：

```python
while condition:
```

通常表示：

```text
只要 condition 成立就继续
```

---

# 12. while 循环要注意更新条件

例如：

```python
n = 10

while n > 0:
    print(n)
```

这里 `n` 永远都是：

```text
10
```

所以：

```python
n > 0
```

永远成立。

最终就会形成：

```text
无限循环 / 死循环
```

因此通常需要在循环内部修改相关变量：

```python
n -= 1
```

完整写法：

```python
n = 10

while n > 0:
    print(n)
    n -= 1
```

---

# 13. break —— 提前结束循环

`break` 用于：

> **立即退出当前循环。**

例如：

```python
for i in range(10):
    if i == 5:
        break

    print(i, end=" ")
```

输出：

```text
0 1 2 3 4
```

执行到：

```text
i = 5
```

时：

```python
if i == 5:
    break
```

条件成立，于是：

```text
循环立即结束
```

后面的：

```text
5 6 7 8 9
```

都不会再执行。

流程：

```text
i = 0 → 输出
i = 1 → 输出
i = 2 → 输出
i = 3 → 输出
i = 4 → 输出
i = 5
  ↓
条件成立
  ↓
break
  ↓
直接退出循环
```

:chatgpt-content-reference{index="9"}

---

# 14. continue —— 跳过本次循环

`continue` 和 `break` 不一样。

```text
break
↓
整个循环结束
```

而：

```text
continue
↓
只结束当前这一轮
↓
继续下一轮
```

例如：

```python
for i in range(10):
    if i % 2 == 0:
        continue

    print(i, end=" ")
```

输出：

```text
1 3 5 7 9
```

这里：

```python
i % 2 == 0
```

用于判断：

```text
i 是否为偶数
```

如果是偶数：

```python
continue
```

直接跳过后面的：

```python
print(i)
```

进入下一轮循环。

因此：

```text
0 → 偶数 → continue → 不输出
1 → 奇数 → 输出
2 → 偶数 → continue → 不输出
3 → 奇数 → 输出
...
```

最终只输出：

```text
1 3 5 7 9
```

:chatgpt-content-reference{index="10"}

---

# 15. break 和 continue 对比

| 关键字 | 作用 |
|---|---|
| `break` | 立即结束整个当前循环 |
| `continue` | 跳过本轮剩余代码，进入下一轮 |

可以简单记成：

```text
break
→ 循环不干了

continue
→ 这一轮不干了，下一轮继续
```

例如：

```python
for i in range(10):
    if i == 5:
        break
```

到 `5`：

```text
整个循环结束
```

而：

```python
for i in range(10):
    if i == 5:
        continue
```

只是：

```text
跳过 i = 5
```

之后仍然会继续：

```text
6 7 8 9
```

---

# 16. for...else

Python 的循环还可以和 `else` 配合：

```python
for 变量 in 可迭代对象:
    ...
else:
    ...
```

这里的 `else` 并不是：

```text
for 条件不成立
```

而是：

> **循环正常结束，并且没有被 `break` 中断时执行。**

例如：

```python
for i in range(5):
    if i == 99:
        break
else:
    print("循环正常结束，没有 break")
```

`range(5)` 只有：

```text
0 1 2 3 4
```

所以：

```python
i == 99
```

永远不会成立。

也就不会执行：

```python
break
```

因此循环正常结束，最后执行：

```python
else:
```

输出：

```text
循环正常结束，没有 break
```

:chatgpt-content-reference{index="11"}

---

# 17. for...else 遇到 break

如果循环中执行了：

```python
break
```

那么 `else` 就不会执行。

例如：

```python
for i in range(5):
    if i == 3:
        break
else:
    print("循环正常结束")
```

执行过程：

```text
i = 0
i = 1
i = 2
i = 3
  ↓
break
  ↓
循环被中断
  ↓
else 不执行
```

因此可以记成：

```text
for 循环
   │
   ├── 正常遍历结束
   │        ↓
   │     执行 else
   │
   └── 遇到 break
            ↓
        不执行 else
```

`for...else` 比较适合用于：

```text
查找目标
   ↓
找到了 → break
没找到 → 循环正常结束 → else
```

:chatgpt-content-reference{index="12"}

---

# 18. Python 没有 do...while

Python 没有：

```text
do...while
```

这种循环结构。

如果需要实现：

> 先执行一次，再判断是否继续。

可以使用：

```python
while True:
    # 至少执行一次

    if 条件:
        break
```

例如：

```python
while True:
    number = int(input("请输入一个正数："))

    if number > 0:
        break
```

执行逻辑：

```text
进入 while True
      ↓
执行循环体
      ↓
判断退出条件
      ↓
满足 → break
      ↓
结束循环
```

---

# 19. Python 没有 i++ 和 i--

Python 不支持：

```python
i++
```

也不支持：

```python
i--
```

需要写成：

```python
i += 1
```

和：

```python
i -= 1
```

例如：

```python
n = 10

while n > 0:
    print(n)
    n -= 1
```

其中：

```python
n -= 1
```

等价于：

```python
n = n - 1
```

---

# 20. range() 不会直接创建完整列表

例如：

```python
range(5)
```

并不是直接创建：

```python
[0, 1, 2, 3, 4]
```

`range()` 返回的是一个 `range` 对象，会按需要产生对应的整数，因此即使范围很大，也不需要先把所有数字完整保存成一个列表。

例如：

```python
r = range(10**9)
```

不会直接创建一个包含十亿个整数的普通列表。

如果确实需要转换成列表，可以使用：

```python
list(range(5))
```

结果：

```python
[0, 1, 2, 3, 4]
```

:chatgpt-content-reference{index="13"}

---

# 21. 嵌套循环中的 break

循环内部还可以继续写循环：

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

这就是：

```text
外层循环
    ↓
内层循环
```

需要注意：

> `break` 只会退出它所在的当前循环。

例如：

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break

    print(i)
```

这里：

```python
break
```

退出的是：

```python
for j in range(3)
```

而不是：

```python
for i in range(3)
```

因此：

```text
外层循环
   ↓
进入内层循环
   ↓
内层遇到 break
   ↓
只退出内层
   ↓
外层继续
```

如果需要退出多层循环，可以根据程序结构使用标志变量，或者将逻辑封装到函数中并使用 `return`。:chatgpt-content-reference{index="14"}

---

# 22. 循环控制整体关系

```text
                    循环
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
      for...in                while
          │                     │
   遍历可迭代对象          条件为 True
          │                 就继续执行
          │
     常配合 range()
          │
          ↓
  range(start, stop, step)
          │
       左闭右开

循环执行过程中
          │
     ┌────┴────┐
     ↓         ↓
   break    continue
     │         │
退出整个      跳过本轮
当前循环      继续下一轮

for 循环还可以配合 else
          │
     ┌────┴────┐
     ↓         ↓
没有 break   遇到 break
     │         │
执行 else   不执行 else
```

---

# 23. 常用写法总结

## 遍历列表

```python
for x in data:
    print(x)
```

## 同时获取索引和值

```python
for i, x in enumerate(data):
    print(i, x)
```

## 按次数循环

```python
for i in range(10):
    print(i)
```

## 指定范围

```python
for i in range(1, 11):
    print(i)
```

## 指定步长

```python
for i in range(0, 10, 2):
    print(i)
```

## 条件循环

```python
while condition:
    ...
```

## 提前结束

```python
if condition:
    break
```

## 跳过本轮

```python
if condition:
    continue
```

---

# 🧠 本节重点总结

| 知识点 | 核心含义 |
|---|---|
| `for...in` | 依次遍历可迭代对象中的元素 |
| `enumerate()` | 遍历时同时获得索引和值 |
| `range(stop)` | 从 `0` 到 `stop - 1` |
| `range(start, stop)` | 从 `start` 到 `stop` 之前 |
| `range(start, stop, step)` | 指定开始、结束和步长 |
| 左闭右开 | 包含 `start`，不包含 `stop` |
| `while` | 条件为 `True` 时持续循环 |
| `break` | 立即退出当前循环 |
| `continue` | 跳过本轮，进入下一轮 |
| `for...else` | 没有被 `break` 中断时执行 `else` |
| `i += 1` | Python 中常用的自增写法 |
| `i -= 1` | Python 中常用的自减写法 |

---

# 🔗 循环整体关系

```text
需要重复执行代码
        │
        ↓
   是否需要遍历对象？
      /       \
    是         否
    ↓           ↓
for...in      while
    │           │
    ↓           ↓
遍历元素      根据条件循环
    │
需要数字范围
    ↓
 range()
    │
    ├── range(stop)
    ├── range(start, stop)
    └── range(start, stop, step)

循环过程中
    │
    ├── break    → 退出循环
    └── continue → 跳过本轮

for 循环结束
    │
    ├── 正常结束 → 可以执行 else
    └── break    → 不执行 else
```

---

# ✅ 本节掌握

学习完本节后，需要能够：

- 使用 `for...in` 遍历列表、字符串等可迭代对象
- 理解 `for` 循环是直接获取元素，而不是必须通过下标访问
- 使用 `enumerate()` 同时获取索引和值
- 掌握 `range()` 的三种基本形式
- 理解 `range()` 的左闭右开规则
- 使用 `for + range()` 完成计数和累加
- 使用 `while` 根据条件控制循环
- 避免因为条件始终成立而产生死循环
- 区分 `break` 和 `continue`
- 理解 `for...else` 的执行条件
- 知道 Python 没有 `do...while`
- 知道 Python 使用 `+= 1`、`-= 1`，而不是 `++`、`--`
- 理解嵌套循环中 `break` 只退出当前所在的循环