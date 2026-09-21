# 02 - 数据类型和变量

## 📌 本节知识点

这一节主要了解 Python 中最基础的数据类型和变量，包括：

- 整数 `int`
- 浮点数 `float`
- 字符串 `str`
- 布尔值 `bool`
- 空值 `None`
- Python 的动态类型
- `type()` 查看数据类型
- 多重赋值
- 变量交换
- 常量的命名约定
- 基本算术运算符
- Python 的变量命名方式

---

# 1. Python 中的基本数据类型

Python 中常见的基本数据类型包括：

| 数据类型 | Python 类型 | 示例 |
| --- | --- | --- |
| 整数 | `int` | `100`、`-20`、`0` |
| 浮点数 | `float` | `3.14`、`1.23e9` |
| 字符串 | `str` | `"hello"` |
| 布尔值 | `bool` | `True`、`False` |
| 空值 | `NoneType` | `None` |

可以使用内置函数 `type()` 查看一个对象的类型：

```python
print(type(42))
print(type(3.14))
print(type("hello"))
print(type(True))
print(type(None))
```

输出：

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

---

# 2. 整数 `int`

Python 使用 `int` 表示整数。

```python
a = 100
b = -8080
```

整数可以是：

```python
100
0
-100
8080
```

## 不同进制的整数

Python 可以直接表示不同进制的整数。

### 十六进制

使用 `0x` 或 `0X` 开头：

```python
c = 0xff00
print(c)
```

输出：

```text
65280
```

也就是说：

```text
0xff00 = 65280
```

### 二进制

使用 `0b` 或 `0B` 开头：

```python
a = 0b1010
print(a)
```

输出：

```text
10
```

### 八进制

使用 `0o` 或 `0O` 开头：

```python
a = 0o12
print(a)
```

输出：

```text
10
```

因此可以简单记为：

```text
二进制：0b
八进制：0o
十六进制：0x
```

---

# 3. Python 整数的大小

Python 的整数不像一些固定宽度整数类型那样受到 32 位、64 位范围的直接限制。

例如：

```python
print(2 ** 100)
```

可以得到：

```text
1267650600228229401496703205376
```

Python 会根据整数大小自动管理所需要的存储空间。

因此，在实际使用中，Python 的 `int` 可以表示非常大的整数，主要受到可用内存等实际资源的限制。

---

# 4. 整数除法

Python 中 `/` 和 `//` 的作用不同。

## `/` 普通除法

```python
print(10 / 3)
```

结果：

```text
3.3333333333333335
```

即使两个操作数都是整数，`/` 得到的结果通常也是浮点数。

例如：

```python
print(10 / 2)
```

结果：

```text
5.0
```

---

## `//` 整除

如果只需要除法结果的整数部分，可以使用：

```python
print(10 // 3)
```

结果：

```text
3
```

需要注意，`//` 更准确地说是**向下取整除法（floor division）**。

例如：

```python
print(-10 // 3)
```

结果：

```text
-4
```

并不是简单地把小数部分删除。

---

# 5. 浮点数 `float`

带有小数的数通常使用 `float` 表示。

例如：

```python
a = 1.23
b = 3.14
c = -0.5
```

查看类型：

```python
print(type(3.14))
```

输出：

```text
<class 'float'>
```

---

# 6. 科学计数法

Python 的浮点数支持科学计数法。

例如：

```python
e = 1.23e9
```

其中：

```text
e9
```

表示：

```text
× 10⁹
```

所以：

```text
1.23e9
```

相当于：

```text
1.23 × 10⁹
```

即：

```text
1230000000.0
```

例如：

```python
print(1.23e9)
```

输出：

```text
1230000000.0
```

---

# 7. 浮点数的精度问题

浮点数不能保证所有十进制小数都能够被二进制精确表示。

经典例子：

```python
print(0.1 + 0.2)
```

结果可能是：

```text
0.30000000000000004
```

而不是：

```text
0.3
```

这并不是 Python 计算错误，而与计算机使用二进制表示浮点数的方式有关。

很多十进制小数在二进制中无法有限表示，因此只能保存一个非常接近真实值的近似值。

可以简单理解为：

```text
十进制小数
    ↓
转换为二进制浮点数
    ↓
部分数字无法精确表示
    ↓
只能保存近似值
    ↓
计算后可能出现微小误差
```

因此：

> 浮点数不适合直接用于要求完全精确的小数计算。

如果以后遇到需要精确十进制计算的情况，可以使用 Python 的 `decimal` 模块。

---

# 8. 字符串 `str`

Python 使用 `str` 表示字符串。

字符串可以使用单引号：

```python
s1 = 'hello'
```

也可以使用双引号：

```python
s2 = "world"
```

例如：

```python
print(s1, s2)
```

输出：

```text
hello world
```

普通情况下：

```python
'hello'
```

和：

```python
"hello"
```

表示的都是字符串。

查看类型：

```python
print(type("hello"))
```

结果：

```text
<class 'str'>
```

---

# 9. 布尔值 `bool`

布尔值用于表示逻辑上的：

```text
真 / 假
```

Python 中分别写成：

```python
True
False
```

注意首字母必须大写。

正确：

```python
True
False
```

不能写成：

```python
true
false
```

例如：

```python
t = True
f = False

print(t)
print(f)
```

输出：

```text
True
False
```

---

# 10. 布尔运算

Python 中常见的三个布尔运算符是：

```text
and
or
not
```

## `and`

只有两边都为 `True`，结果才为 `True`。

```python
print(True and True)
print(True and False)
```

输出：

```text
True
False
```

---

## `or`

只要其中一个为 `True`，结果就为 `True`。

```python
print(True or False)
print(False or False)
```

输出：

```text
True
False
```

---

## `not`

用于取反：

```python
print(not True)
print(not False)
```

输出：

```text
False
True
```

可以总结为：

| 表达式 | 结果 |
| --- | --- |
| `True and True` | `True` |
| `True and False` | `False` |
| `False and False` | `False` |
| `True or False` | `True` |
| `False or False` | `False` |
| `not True` | `False` |
| `not False` | `True` |

---

# 11. `bool` 与 `int` 的关系

Python 中 `bool` 是 `int` 的子类。

在数值环境下：

```text
True  → 1
False → 0
```

例如：

```python
print(True + True)
```

结果：

```text
2
```

因为在这个计算中可以理解为：

```text
1 + 1 = 2
```

不过实际编程中通常不会故意利用这种写法进行普通数学计算，布尔值主要还是用于逻辑判断。

---

# 12. `None`

Python 使用：

```python
None
```

表示一个特殊的空值。

例如：

```python
n = None
print(n)
```

输出：

```text
None
```

查看类型：

```python
print(type(None))
```

结果：

```text
<class 'NoneType'>
```

因此：

```text
None       → 一个特殊的空值
NoneType   → None 所属的类型
```

需要注意：

```python
None
```

并不等于：

```python
0
```

也不等于：

```python
""
```

它们表示的是不同的对象。

---

# 13. 变量

变量可以理解为一个**名字**，这个名字引用了某个对象。

例如：

```python
x = 10
```

可以简单理解为：

```text
x ─────→ 10
```

这里：

```text
x
```

是变量名，而：

```text
10
```

是一个整数对象。

---

# 14. Python 不需要提前声明变量类型

Python 创建变量时不需要写：

```text
int
float
string
```

可以直接赋值：

```python
x = 10
name = "Python"
pi = 3.14
```

Python 会根据当前引用的对象确定类型。

例如：

```python
x = 10
print(type(x))
```

结果：

```text
<class 'int'>
```

---

# 15. Python 是动态类型语言

同一个变量可以先后引用不同类型的对象。

例如：

```python
x = 10
print(type(x))

x = "hello"
print(type(x))
```

结果：

```text
<class 'int'>
<class 'str'>
```

可以理解为：

第一次：

```text
x ─────→ 10
          int
```

重新赋值之后：

```text
x ─────→ "hello"
          str
```

并不是 `x` 自己从整数“变成”了字符串，而是：

> `x` 这个名字重新引用了另一个对象。

因此 Python 中更准确的理解是：

```text
变量名 → 对象
```

而不是：

```text
变量里面固定装着某一种类型的数据
```

---

# 16. 动态类型的特点

动态类型使代码写起来比较灵活：

```python
x = 100
x = "hello"
x = True
```

这些写法都是允许的。

但是也意味着某些类型错误可能直到程序运行到对应代码时才被发现。

例如：

```python
x = "hello"
print(x / 2)
```

字符串不能直接进行这种除法运算，因此运行到这一行时会发生类型错误。

所以在较大的 Python 项目中，经常会使用**类型注解（Type Hints）**帮助说明变量和函数预期的数据类型。

---

# 17. `type()` 查看类型

Python 内置的：

```python
type()
```

可以查看一个对象的类型。

例如：

```python
print(type(42))
print(type(3.14))
print(type("hello"))
print(type(True))
print(type(None))
```

输出：

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

如果不确定某个变量当前引用的对象是什么类型，也可以：

```python
x = 100
print(type(x))
```

---

# 18. 多重赋值

Python 支持一次给多个变量赋值。

例如：

```python
a, b, c = 1, 2, 3
```

相当于分别得到：

```text
a = 1
b = 2
c = 3
```

输出：

```python
print(a, b, c)
```

结果：

```text
1 2 3
```

这种写法称为多重赋值。

---

# 19. 交换两个变量

Python 可以非常方便地交换两个变量的值。

例如：

```python
a = 1
b = 2

a, b = b, a

print(a, b)
```

输出：

```text
2 1
```

交换前：

```text
a = 1
b = 2
```

执行：

```python
a, b = b, a
```

之后：

```text
a = 2
b = 1
```

不需要额外创建临时变量。

可以先简单理解为：

```text
先取得右边的 b 和 a
        ↓
形成新的两个值
        ↓
分别赋给左边的 a 和 b
```

---

# 20. Python 中的常量

Python 没有通过普通变量语法强制一个变量赋值后永远不能修改的机制。

通常使用：

> **全大写变量名表示这个值按照约定不应该被修改。**

例如：

```python
PI = 3.14159265
MAX_SIZE = 100
```

看到：

```text
PI
MAX_SIZE
```

这种全大写名称时，一般表示程序将其作为常量使用。

但是 Python 本身仍然允许重新赋值：

```python
PI = 3
```

因此，全大写是一种**代码规范和约定**，而不是 Python 强制的限制。

---

# 21. 常见算术运算符

这一节涉及几个常见的 Python 算术运算符：

| 运算符 | 含义 | 示例 | 结果 |
| --- | --- | --- | --- |
| `+` | 加法 | `2 + 3` | `5` |
| `-` | 减法 | `5 - 2` | `3` |
| `*` | 乘法 | `2 * 3` | `6` |
| `/` | 普通除法 | `10 / 3` | `3.333...` |
| `//` | 向下取整除法 | `10 // 3` | `3` |
| `%` | 取余 | `10 % 3` | `1` |
| `**` | 幂运算 | `2 ** 10` | `1024` |

例如：

```python
print(2 ** 10)
```

表示：

```text
2¹⁰
```

结果：

```text
1024
```

---

# 22. Python 中一切皆对象

Python 中的数据都可以看作对象。

例如：

```python
42
```

不仅仅是一个单纯的数字，它是一个 `int` 对象。

因此可以调用属于整数对象的方法：

```python
print((42).bit_length())
```

`bit_length()` 可以得到表示这个整数所需要的二进制位数。

这体现了 Python 中一个很重要的思想：

> Python 中的数据通常都是对象，对象可以具有自己的属性和方法。

这一点后面学习类、对象和面向对象编程时会更加重要。

---

# 23. Python 变量命名

Python 中变量名通常使用**蛇形命名法（snake_case）**。

例如：

```python
max_size = 100
user_name = "Tom"
student_age = 20
```

多个单词之间使用：

```text
_
```

连接。

推荐：

```python
max_size
student_name
user_age
```

而普通变量一般不使用：

```python
maxSize
studentName
```

Python 的代码风格规范 PEP 8 通常推荐函数名和变量名使用小写字母，并用下划线分隔单词。

---

# 🧠 本节重点总结

## 五种基本数据类型

```text
int       → 整数
float     → 浮点数
str       → 字符串
bool      → 布尔值
NoneType  → None 的类型
```

---

## 整数

```python
a = 100
b = -8080
c = 0xff00
```

支持：

```text
0b → 二进制
0o → 八进制
0x → 十六进制
```

Python 的整数可以表示非常大的数。

---

## 浮点数

```python
a = 3.14
b = 1.23e9
```

需要注意浮点数存在精度问题：

```python
0.1 + 0.2
```

可能得到：

```text
0.30000000000000004
```

---

## 字符串

```python
"hello"
'hello'
```

单引号和双引号都可以表示字符串。

---

## 布尔值

只有：

```python
True
False
```

注意首字母大写。

常见逻辑运算：

```python
and
or
not
```

---

## None

```python
x = None
```

表示一个特殊的空值：

```python
type(None)
```

得到：

```text
NoneType
```

---

## 动态类型

Python 不需要提前声明变量类型：

```python
x = 10
x = "hello"
```

更准确地理解为：

```text
变量名 → 对象
```

变量名可以重新引用不同类型的对象。

---

## 查看类型

```python
type(x)
```

例如：

```python
type(100)       # int
type(3.14)      # float
type("hello")   # str
type(True)      # bool
type(None)      # NoneType
```

---

## 多重赋值

```python
a, b, c = 1, 2, 3
```

---

## 变量交换

```python
a, b = b, a
```

不需要额外的临时变量。

---

## 常量约定

```python
PI = 3.14159265
MAX_SIZE = 100
```

全大写表示按照约定将其作为常量使用，但 Python 本身不会禁止重新赋值。

---

## 常见运算符

```text
/   → 普通除法
//  → 向下取整除法
%   → 取余
**  → 幂运算
```

---

## 变量命名

推荐使用蛇形命名：

```python
student_name
max_size
user_age
```

---

# ✅ 本节掌握

完成这一部分后，需要能够理解和使用：

- `int`、`float`、`str`、`bool` 和 `None`
- 二进制、八进制和十六进制整数的基本写法
- `/` 与 `//` 的区别
- `**` 和 `%` 的作用
- 浮点数为什么可能存在精度误差
- `True`、`False` 以及 `and`、`or`、`not`
- `None` 与 `NoneType`
- Python 的动态类型特点
- “变量名引用对象”的基本理解
- 使用 `type()` 查看对象类型
- 多重赋值
- 使用 `a, b = b, a` 交换变量
- Python 的常量命名约定
- Python 中“一切皆对象”的基本概念
- 使用 `snake_case` 命名变量s