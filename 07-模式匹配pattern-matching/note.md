# 07 - 模式匹配 Pattern Matching

## 📌 本节知识点

这一节主要学习 Python 中的模式匹配 `match/case`，包括：

- `match/case` 的基本概念
- `match/case` 的基本语法
- Python 版本要求
- 常量匹配
- `case _` 通配符
- 多值匹配 `|`
- `match/case` 的执行顺序
- 序列匹配
- 序列解构
- 模式中的变量绑定
- 捕获变量与通配符的区别
- 条件守卫 Guard
- `match/case` 与 `if/elif/else` 的区别
- `match/case` 的适用场景

---

# 1. 模式匹配 `match/case`

Python 从：

```text
Python 3.10
```

开始支持：

```python
match
case
```

模式匹配语法。

它可以根据一个值或者数据的结构，选择对应的分支执行。

例如：

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Unknown status: {status}")
```

这里：

```text
status = 404
```

所以最终匹配：

```python
case 404:
```

输出：

```text
Not Found
```

---

# 2. `match/case` 的基本结构

基本格式：

```python
match 要匹配的对象:
    case 模式1:
        代码1
    case 模式2:
        代码2
    case 模式3:
        代码3
```

可以理解为：

```text
          match value
               │
       ┌───────┼───────┐
       │       │       │
    case A   case B   case C
       │       │       │
       ↓       ↓       ↓
    代码 A   代码 B   代码 C
```

其中：

```python
match value:
```

表示：

```text
对 value 进行模式匹配
```

而：

```python
case pattern:
```

表示：

```text
尝试使用 pattern 匹配 value
```

---

# 3. Python 版本要求

`match/case` 是：

```text
Python 3.10+
```

加入的语法。

因此：

```text
Python 3.10
Python 3.11
Python 3.12
...
```

都可以使用。

如果 Python 版本低于：

```text
3.10
```

则不能直接使用 `match/case`。

可以先通过：

```bash
python --version
```

查看 Python 版本。

---

# 4. 常量匹配

最基本的 `match/case` 可以用于匹配具体的值。

例如：

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
```

这里的：

```python
200
404
500
```

都是具体的常量。

执行过程：

```text
status = 404
     ↓
match status
     ↓
case 200 ?  → 不匹配
     ↓
case 404 ?  → 匹配
     ↓
Not Found
```

因此：

```python
case 404:
```

表示：

```text
当匹配对象符合 404 这个模式时，执行对应代码
```

---

# 5. `match/case` 从上到下匹配

`match/case` 会按照：

```text
从上到下
```

依次尝试每一个 `case`。

例如：

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
```

执行顺序：

```text
match status
     ↓
case 200
     ↓
不匹配
     ↓
case 404
     ↓
匹配
     ↓
执行对应代码
```

因此：

```text
从上到下尝试匹配
        ↓
找到第一个匹配的 case
        ↓
执行对应代码块
        ↓
结束整个 match
```

---

# 6. 命中一个 `case` 后停止

当某一个 `case` 匹配成功以后，不会继续执行后面的其他 `case`。

例如：

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")
```

匹配：

```python
case 404:
```

之后输出：

```text
Not Found
```

然后结束整个 `match`。

不会继续执行：

```python
case _:
```

因此：

```text
match/case
    ↓
命中第一个匹配项
    ↓
执行
    ↓
停止
```

---

# 7. `case _` 通配符

如果前面的模式全部没有匹配，可以使用：

```python
case _:
```

处理其他情况。

例如：

```python
status = 403

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Unknown status: {status}")
```

因为：

```text
403 ≠ 200
403 ≠ 404
403 ≠ 500
```

所以最终匹配：

```python
case _:
```

输出：

```text
Unknown status: 403
```

---

# 8. `_` 表示匹配其他情况

在模式匹配中：

```text
_
```

是一个特殊的通配符。

可以理解为：

```text
其他任意情况
```

因此：

```python
case _:
```

通常放在最后。

整个结构可以表示为：

```text
case 200
   ↓
不匹配

case 404
   ↓
不匹配

case 500
   ↓
不匹配

case _
   ↓
其他情况全部匹配
```

因此它的作用和条件判断中的：

```python
else:
```

有些类似。

可以先记成：

```text
if/elif/else 中：

else → 处理前面条件都不满足的情况


match/case 中：

case _ → 处理前面模式都不匹配的情况
```

---

# 9. 多值匹配 `|`

一个 `case` 还可以同时匹配多个值。

使用：

```text
|
```

连接多个模式。

例如：

```python
command = "quit"

match command:
    case "quit" | "exit" | "q":
        print("退出程序")
    case "help" | "h":
        print("显示帮助")
    case _:
        print(f"未知命令: {command}")
```

这里：

```python
case "quit" | "exit" | "q":
```

表示：

```text
"quit"
或者
"exit"
或者
"q"
```

其中任意一个匹配都可以进入这个分支。

---

# 10. `|` 的含义

例如：

```python
case "quit" | "exit" | "q":
```

可以理解为：

```text
command == "quit"
        或
command == "exit"
        或
command == "q"
```

因此：

```text
command = "quit"
```

会匹配。

```text
command = "exit"
```

也会匹配。

```text
command = "q"
```

同样会匹配。

可以记成：

```text
pattern1 | pattern2 | pattern3

              ↓

       匹配其中任意一个
```

---

# 11. 多值匹配示例

例如：

```python
command = "help"

match command:
    case "quit" | "exit" | "q":
        print("退出程序")
    case "help" | "h":
        print("显示帮助")
    case _:
        print("未知命令")
```

执行过程：

```text
command = "help"
       ↓
"quit" | "exit" | "q"
       ↓
     不匹配
       ↓
   "help" | "h"
       ↓
      匹配
       ↓
    显示帮助
```

这样可以避免为多个相同处理结果分别写多个 `case`。

---

# 12. `match/case` 不只能匹配简单值

`match/case` 和普通的值判断不同，它不仅可以判断：

```text
这个值是不是 404
```

还可以根据数据的：

```text
结构
```

进行匹配。

例如：

```python
point = (0, 5)
```

这是一个包含两个元素的元组。

可以直接：

```python
match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"在 x 轴上, x={x}")
    case (0, y):
        print(f"在 y 轴上, y={y}")
    case (x, y):
        print(f"任意点: ({x}, {y})")
```

这里匹配的不只是一个具体值，还包括：

```text
元组的结构
+
元组内部元素的值
```

---

# 13. 序列匹配

例如：

```python
point = (0, 5)
```

模式：

```python
case (0, 0):
```

表示：

```text
这是一个包含两个元素的序列
并且
第一个元素是 0
第二个元素也是 0
```

也就是：

```text
(0, 0)
```

如果：

```python
point = (0, 0)
```

就会匹配：

```python
case (0, 0):
    print("原点")
```

---

# 14. 序列解构

模式匹配还可以在匹配数据结构的同时，把其中的数据提取出来。

例如：

```python
case (x, 0):
```

这里：

```text
(x, 0)
```

表示：

```text
这是一个两元素序列
       +
第二个元素必须是 0
       +
第一个元素保存到变量 x
```

例如：

```python
point = (5, 0)
```

匹配：

```python
case (x, 0):
```

之后：

```text
x = 5
```

因此可以使用：

```python
print(f"在 x 轴上, x={x}")
```

输出：

```text
在 x 轴上, x=5
```

---

# 15. `(0, y)` 的匹配过程

例如：

```python
point = (0, 5)
```

匹配：

```python
case (0, y):
```

这个模式要求：

```text
第一个元素必须是 0
第二个元素可以是其他值
并且把第二个元素保存到 y
```

所以：

```text
point = (0, 5)
          │  │
          │  └────→ y = 5
          │
          └───────→ 必须等于 0
```

最终：

```text
y = 5
```

执行：

```python
print(f"在 y 轴上, y={y}")
```

输出：

```text
在 y 轴上, y=5
```

---

# 16. `(x, y)` 匹配任意二维点

例如：

```python
case (x, y):
    print(f"任意点: ({x}, {y})")
```

这里没有要求：

```text
x 必须等于某个固定值
y 必须等于某个固定值
```

而是将两个元素分别绑定到：

```text
x
y
```

例如：

```python
point = (3, 7)
```

匹配之后：

```text
x = 3
y = 7
```

输出：

```text
任意点: (3, 7)
```

---

# 17. 二维坐标匹配关系

这一组代码可以统一理解为：

```python
match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"在 x 轴上, x={x}")
    case (0, y):
        print(f"在 y 轴上, y={y}")
    case (x, y):
        print(f"任意点: ({x}, {y})")
```

对应：

```text
point
  │
  ├── (0, 0)
  │      ↓
  │     原点
  │
  ├── (x, 0)
  │      ↓
  │     x 轴
  │
  ├── (0, y)
  │      ↓
  │     y 轴
  │
  └── (x, y)
         ↓
       任意点
```

---

# 18. 模式的顺序仍然很重要

由于：

```text
match/case 从上到下匹配
```

所以模式的顺序也会影响结果。

例如：

```python
point = (0, 5)
```

如果先写：

```python
case (x, y):
```

那么：

```text
(0, 5)
```

已经能够匹配：

```text
x = 0
y = 5
```

后面的：

```python
case (0, y):
```

就不会再执行。

因此通常应该：

```text
更具体的模式放前面
更宽泛的模式放后面
```

例如：

```text
(0, 0)    ← 最具体

(x, 0)
(0, y)

(x, y)    ← 更宽泛
```

---

# 19. 模式中的变量绑定

在：

```python
case (x, y):
```

中：

```text
x
y
```

不是在判断变量 `x`、`y` 原来等于什么。

这里的作用是：

```text
捕获匹配到的数据
```

例如：

```python
point = (3, 8)
```

执行：

```python
case (x, y):
```

会得到：

```text
x = 3
y = 8
```

这种行为称为：

```text
变量绑定
```

或者：

```text
捕获
```

---

# 20. `case x` 与 `case _` 的区别

这两个写法看起来都可以匹配很多情况：

```python
case x:
```

和：

```python
case _:
```

但是作用不同。

### `case x`

```python
case x:
```

会匹配一个值，并把这个值绑定给：

```text
x
```

例如：

```text
value = 100
```

匹配后：

```text
x = 100
```

---

### `case _`

```python
case _:
```

表示：

```text
其他任意情况
```

但不会把这个值作为普通捕获变量保存到 `_` 中使用。

因此可以简单记成：

```text
case x
   ↓
匹配 + 保存到 x


case _
   ↓
只负责兜底匹配
```

---

# 21. 条件守卫 Guard

有时只靠模式还不能完整表达条件。

这时可以在 `case` 后面继续添加：

```python
if 条件
```

这种写法称为：

```text
条件守卫
```

英文：

```text
Guard
```

例如：

```python
age = 15

match age:
    case n if n < 0:
        print("年龄不能为负")
    case n if n < 18:
        print(f"{n} 岁，未成年")
    case n if n < 60:
        print(f"{n} 岁，成年人")
    case _:
        print("老年人")
```

---

# 22. `case n if ...` 的含义

例如：

```python
case n if n < 18:
```

可以拆成两部分：

```text
case n
```

表示：

```text
把匹配到的值绑定给 n
```

然后：

```text
if n < 18
```

表示：

```text
额外要求 n < 18
```

因此：

```python
case n if n < 18:
```

可以理解为：

```text
先匹配并得到 n
      ↓
再判断 n < 18
      ↓
条件成立才真正命中
```

---

# 23. 条件守卫的执行过程

例如：

```python
age = 15
```

执行：

```python
match age:
    case n if n < 0:
        print("年龄不能为负")
    case n if n < 18:
        print(f"{n} 岁，未成年")
    case n if n < 60:
        print(f"{n} 岁，成年人")
    case _:
        print("老年人")
```

判断过程：

```text
age = 15
   ↓
n = 15
   ↓
n < 0 ?
   ↓
False
   ↓
n < 18 ?
   ↓
True
   ↓
15 岁，未成年
```

命中以后停止继续匹配。

---

# 24. Guard 中条件顺序同样重要

例如：

```python
match age:
    case n if n < 0:
        ...
    case n if n < 18:
        ...
    case n if n < 60:
        ...
    case _:
        ...
```

这里按照从上到下的顺序可以得到：

```text
n < 0
↓
负数


前面不满足，并且 n < 18
↓
0 ~ 17


前面不满足，并且 n < 60
↓
18 ~ 59


前面全部不满足
↓
其他情况
```

所以虽然代码中只写了：

```python
n < 60
```

但由于前面的：

```python
n < 18
```

已经提前处理，因此执行到这里时实际上已经排除了：

```text
n < 18
```

这种写法和上一节 `if/elif/else` 的多分支判断逻辑比较相似。

---

# 25. `match/case` 与 `if/elif/else`

上一节学习的：

```python
if
elif
else
```

也可以实现多分支判断。

例如：

```python
if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Internal Server Error")
else:
    print("Unknown")
```

可以使用 `match/case` 写成：

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown")
```

---

# 26. 两种条件结构的关系

对于简单的固定值判断：

```text
if status == 200
elif status == 404
elif status == 500
else
```

可以对应：

```text
case 200
case 404
case 500
case _
```

关系可以表示为：

```text
if / elif / else             match / case

if value == A       ←→       case A

elif value == B     ←→       case B

else                ←→       case _
```

但是 `match/case` 不只是另一种 `if/elif` 写法。

它还支持：

```text
序列解构
变量绑定
模式匹配
条件守卫
```

---

# 27. `match/case` 的主要特点

可以把这一节的 `match/case` 能力整理为：

```text
match/case
    │
    ├── 常量匹配
    │
    │   case 404
    │
    ├── 多值匹配
    │
    │   case "q" | "quit"
    │
    ├── 通配符
    │
    │   case _
    │
    ├── 序列解构
    │
    │   case (x, y)
    │
    └── 条件守卫
        │
        case n if n < 18
```

所以模式匹配不仅可以：

```text
判断一个值
```

还可以：

```text
检查数据结构
+
提取其中的数据
+
添加额外条件
```

---

# 28. 什么时候适合使用 `match/case`

如果主要是在判断：

```text
同一个对象属于哪一种模式
```

可以考虑使用：

```python
match/case
```

例如：

```text
状态码分类
命令分类
序列结构匹配
不同数据结构的处理
```

如果只是简单判断一个条件是否成立，例如：

```python
age >= 18
```

直接使用：

```python
if age >= 18:
```

通常就已经足够。

因此可以先建立这样的理解：

```text
普通条件判断
      ↓
if / elif / else


针对一个对象进行多种模式匹配
      ↓
match / case
```

---

# 🧠 本节重点总结

## `match/case`

基本结构：

```python
match value:
    case pattern1:
        ...
    case pattern2:
        ...
    case _:
        ...
```

执行逻辑：

```text
match value
     ↓
从上到下匹配 case
     ↓
找到第一个匹配项
     ↓
执行对应代码
     ↓
结束
```

---

## Python 版本

`match/case` 需要：

```text
Python 3.10+
```

低于 Python 3.10 的版本不能直接使用这一语法。

---

## 常量匹配

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
```

表示：

```text
status == 200
      ↓
case 200


status == 404
      ↓
case 404
```

---

## 通配符 `_`

```python
case _:
```

表示：

```text
其他情况
```

通常作为最后的兜底分支。

可以对应理解为：

```text
if/elif/else 中的 else
```

---

## 多值匹配

```python
case "quit" | "exit" | "q":
```

表示：

```text
"quit"
   或
"exit"
   或
"q"
```

其中任何一个匹配都可以进入该分支。

---

## 序列解构

例如：

```python
case (x, 0):
```

表示：

```text
匹配两个元素的序列
       ↓
第二个元素必须是 0
       ↓
第一个元素保存到 x
```

例如：

```text
(5, 0)
 ↓
x = 5
```

---

## 变量绑定

```python
case (x, y):
```

匹配：

```text
(3, 7)
```

之后：

```text
x = 3
y = 7
```

因此模式中的变量可以用于：

```text
匹配数据
+
提取数据
```

---

## `case x` 和 `case _`

```text
case x
  ↓
匹配并把值绑定给 x


case _
  ↓
通配其他情况
不作为普通捕获变量使用
```

---

## 条件守卫 Guard

```python
case n if n < 18:
```

可以理解为：

```text
匹配并得到 n
      ↓
判断 n < 18
      ↓
True
      ↓
匹配成功
```

因此：

```text
模式 + if 条件
```

就是：

```text
条件守卫
```

---

## 模式顺序

由于：

```text
从上到下匹配
```

所以通常应该：

```text
具体模式
   ↓
一般模式
   ↓
通配模式
```

例如：

```text
case (0, 0)
case (x, 0)
case (0, y)
case (x, y)
```

如果把：

```python
case (x, y):
```

放得太靠前，后面更加具体的二维坐标模式就可能没有机会被匹配。

---

# 🔗 `match/case` 整体关系

这一节的知识可以统一整理为：

```text
                         match value
                              │
                              ↓
                    从上到下尝试 case
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
       常量匹配             多值匹配            序列匹配
          │                   │                   │
      case 404       case "a" | "b"         case (x, y)
          │                   │                   │
          │                   │                   ↓
          │                   │               解构 + 绑定
          │                   │
          └───────────────────┼───────────────────┐
                              │                   │
                              ↓                   ↓
                         条件守卫              case _
                              │                   │
                     case n if ...             通配符
                              │                   │
                              └─────────┬─────────┘
                                        ↓
                               找到第一个匹配项
                                        ↓
                                   执行代码
                                        ↓
                                      结束
```

与上一节的条件判断可以建立关系：

```text
if / elif / else
        │
        ↓
根据 True / False 选择分支


match / case
        │
        ↓
根据值或数据结构进行模式匹配
```

---

# ✅ 本节掌握

完成这一部分后，需要能够理解和使用：

- 理解模式匹配的基本作用
- 知道 `match/case` 从 Python 3.10 开始支持
- 掌握 `match value:` 的基本结构
- 掌握 `case pattern:` 的基本结构
- 理解 `match/case` 从上到下进行匹配
- 理解命中第一个 `case` 后停止继续匹配
- 使用 `case 200:` 等形式进行常量匹配
- 使用 `case _:` 处理其他情况
- 理解 `_` 是模式匹配中的通配符
- 使用 `|` 在一个 `case` 中匹配多个值
- 理解 `"a" | "b"` 表示匹配其中任意一种模式
- 理解 `match/case` 不只是简单的值比较
- 使用 `(0, 0)` 匹配固定结构
- 使用 `(x, 0)` 进行序列匹配和变量绑定
- 使用 `(0, y)` 提取序列中的数据
- 使用 `(x, y)` 解构二维序列
- 理解模式中的变量具有捕获和绑定数据的作用
- 理解 `case x` 与 `case _` 的区别
- 理解模式顺序会影响最终匹配结果
- 知道更加具体的模式通常应该放在更加宽泛的模式前面
- 理解条件守卫 Guard 的作用
- 使用 `case n if 条件:` 添加额外判断
- 理解 Guard 是“模式匹配 + 额外条件”
- 理解 `match/case` 与 `if/elif/else` 的联系
- 理解 `case _` 与 `else` 在兜底处理上的相似之处
- 能够根据实际判断方式选择 `if/elif/else` 或 `match/case`