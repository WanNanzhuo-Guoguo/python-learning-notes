# 01 - Hello World

## 📌 本节知识点

这一节主要了解 Python 程序最基本的运行方式，包括：

- Python 程序的基本形式
- `print()` 函数的使用
- Python 中字符串的基本写法
- 单引号与双引号的区别
- Python 代码中的标点符号
- 交互模式（REPL）与脚本模式
- Python 文件的基本规则
- Python 程序的执行方式

---

## 1. 第一个 Python 程序

最简单的 Python 程序：

```python
print("hello, world")
```

运行结果：

```text
hello, world
```

Python 不要求必须编写 `main()` 函数，也不需要额外的程序入口结构。

因此：

```python
print("hello, world")
```

本身就是一个可以直接运行的完整 Python 程序。

---

## 2. `print()` 函数

`print()` 是 Python 的内置函数，主要作用是将指定内容输出到终端。

基本格式：

```python
print(要输出的内容)
```

例如：

```python
print("hello")
```

输出：

```text
hello
```

### 输出数字和表达式

`print()` 不仅可以输出字符串，也可以输出数字以及表达式的计算结果。

```python
print(100)
print(100 + 200)
```

输出：

```text
100
300
```

其中：

```python
print(100 + 200)
```

会先计算：

```text
100 + 200 = 300
```

然后再将结果 `300` 输出。

---

## 3. `print()` 输出多个内容

可以在一个 `print()` 中使用逗号 `,` 分隔多个内容：

```python
print("1 + 2 =", 1 + 2)
```

输出：

```text
1 + 2 = 3
```

使用逗号分隔多个值时，`print()` 默认会在它们之间加入空格。

例如：

```python
print("hello", "world")
```

输出：

```text
hello world
```

---

## 4. `print()` 默认会换行

`print()` 输出完成之后，默认会在末尾添加换行。

例如：

```python
print("hello")
print("world")
```

输出：

```text
hello
world
```

如果不希望输出后自动换行，可以使用 `end` 参数：

```python
print("hello", end="")
print("world")
```

输出：

```text
helloworld
```

也可以自己指定结尾内容：

```python
print("hello", end=" ")
print("world")
```

输出：

```text
hello world
```

---

## 5. Python 中的字符串

用引号包起来的文本称为字符串。

例如：

```python
"hello"
"Python"
"hello, world"
```

Python 中既可以使用单引号 `' '`，也可以使用双引号 `" "` 表示字符串。

```python
print('hello')
print("hello")
```

两种写法的结果相同：

```text
hello
hello
```

也就是说，对于普通字符串：

```python
'hello'
```

和：

```python
"hello"
```

表示的是相同类型的数据。

---

## 6. 单引号和双引号的选择

虽然单引号和双引号都可以表示字符串，但当字符串本身包含引号时，可以选择另一种引号作为字符串边界，使代码更加简单。

### 字符串中包含单引号

```python
print("I'm learning Python")
```

外面使用双引号，这样字符串中的 `'` 就可以直接使用。

### 字符串中包含双引号

```python
print('He said "hello"')
```

外面使用单引号，这样字符串中的 `"` 就可以直接使用。

因此可以根据字符串中的实际内容选择单引号或双引号。

---

## 7. 注意中英文标点

编写 Python 代码时，需要特别注意输入法。

代码中的括号、引号、逗号、冒号等符号应该使用**英文半角符号**。

### 错误示例

```python
print（"hello"）
```

这里使用的是中文括号：

```text
（ ）
```

而不是英文括号：

```text
( )
```

可能导致：

```text
SyntaxError
```

### 正确写法

```python
print("hello")
```

因此编写代码时最好将输入法切换到英文状态，避免误输入中文标点。

---

## 8. Python 的两种常见运行方式

Python 代码主要可以通过两种方式运行：

1. 交互模式（REPL）
2. 脚本模式

---

### 8.1 交互模式（REPL）

在终端中输入：

```bash
python
```

进入 Python 交互环境后，会看到类似：

```text
>>>
```

此时可以直接输入 Python 代码：

```python
>>> 100 + 200
300
```

也可以：

```python
>>> print("hello")
hello
```

交互模式的特点是：

> 输入一条代码，立即执行一条代码。

因此比较适合：

- 测试简单表达式
- 验证某个 Python 语法
- 快速查看计算结果
- 做一些临时实验

---

### 8.2 脚本模式

实际编写程序时，通常会把 Python 代码保存在 `.py` 文件中。

例如：

```text
hello-world.py
```

文件内容：

```python
print("hello, world")
```

然后在终端执行：

```bash
python hello-world.py
```

输出：

```text
hello, world
```

这种方式就是脚本模式。

---

## 9. 交互模式与脚本模式的重要区别

交互模式会自动显示表达式的结果。

例如：

```python
>>> 100 + 200
300
```

但是在 `.py` 文件中直接写：

```python
100 + 200
```

运行程序时不会显示：

```text
300
```

因为在脚本模式下，这条语句只是完成了计算，并没有要求程序将结果输出到终端。

如果希望看到结果，需要：

```python
print(100 + 200)
```

因此可以记住：

> **计算和输出是两件不同的事情。**

```python
100 + 200
```

表示计算。

```python
print(100 + 200)
```

表示计算之后，再将结果输出。

---

## 10. Python 文件

Python 源代码文件通常使用：

```text
.py
```

作为文件扩展名。

例如：

```text
hello.py
```

或者：

```text
hello_world.py
```

文件名通常建议：

- 使用英文
- 使用小写字母
- 多个单词可以使用下划线 `_`
- 尽量不要使用空格
- 尽量避免中文文件名

例如：

```text
hello_world.py
```

是一种比较常见的命名方式。

---

## 11. Python 不需要在每行末尾写分号

Python 通常使用换行来区分不同语句。

例如：

```python
print("hello")
print("world")
```

不需要写成：

```python
print("hello");
print("world");
```

虽然部分情况下 Python 允许使用分号，但正常编写 Python 程序时通常不需要在每条语句后添加 `;`。

---

## 12. Python 程序的基本执行过程

执行：

```bash
python hello-world.py
```

可以简单理解为：

```text
hello-world.py
        ↓
Python 解释器读取代码
        ↓
按照程序顺序执行
        ↓
print() 执行
        ↓
终端显示 hello, world
```

与 C、C++ 等通常需要先生成可执行文件再运行的开发流程不同，日常使用 Python 时通常可以直接通过 Python 解释器运行 `.py` 文件：

```bash
python 文件名.py
```

---

## 13. PyCharm 中运行 Python

在 PyCharm 中，可以直接打开对应的 `.py` 文件，然后点击右上角的运行按钮：

```text
▶ Run
```

例如运行：

```text
hello-world.py
```

PyCharm 本质上仍然是在使用当前项目配置的 Python Interpreter 来执行这个文件。

也可以使用 PyCharm 自带的 Terminal：

```bash
python hello-world.py
```

因此两种方式本质上都是使用 Python 解释器运行 Python 文件。

---

## 🧠 本节重点总结

### `print()`

用于将内容输出到终端：

```python
print("hello")
```

---

### 输出表达式结果

```python
print(100 + 200)
```

输出：

```text
300
```

---

### 输出多个内容

```python
print("1 + 2 =", 1 + 2)
```

输出：

```text
1 + 2 = 3
```

---

### 字符串

单引号和双引号都可以表示字符串：

```python
'hello'
"hello"
```

---

### 默认换行

```python
print("hello")
print("world")
```

输出：

```text
hello
world
```

可以使用 `end` 修改结尾：

```python
print("hello", end="")
```

---

### 交互模式

```bash
python
```

进入：

```text
>>>
```

特点：

```text
输入一行 → 执行一行 → 立即看到结果
```

---

### 脚本模式

代码保存在：

```text
xxx.py
```

通过：

```bash
python xxx.py
```

运行整个程序。

脚本模式下：

```python
100 + 200
```

不会自动显示结果。

需要：

```python
print(100 + 200)
```

---

### 标点符号

Python 代码中的符号注意使用英文半角形式：

```text
()  ""  ''  ,  :
```

避免误输入：

```text
（） “” ， ：
```

---

## ✅ 本节掌握

完成这一部分后，需要能够理解：

- `print()` 的基本作用
- 如何输出字符串、数字和表达式
- 如何一次输出多个值
- `print()` 默认换行以及 `end` 参数的作用
- Python 字符串可以使用单引号或双引号
- 为什么代码中要注意中英文标点
- 什么是 Python 交互模式（REPL）
- 什么是 Python 脚本模式
- 为什么脚本中的表达式不会自动显示结果
- `.py` 文件的作用
- 如何通过 `python xxx.py` 运行 Python 程序
- PyCharm 的 Run 与终端运行之间的关系