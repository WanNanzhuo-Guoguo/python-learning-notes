# 03 - 字符串和编码

## 📌 本节知识点

这一节主要学习 Python 字符串以及字符编码相关知识，包括：

- 字符串的基本表示方式
- 转义字符
- 原始字符串 `r"..."`
- 多行字符串
- 字符串的不可变性
- 字符与编码的关系
- ASCII、Unicode 和 UTF-8
- `ord()` 与 `chr()`
- `str` 与 `bytes`
- `encode()` 与 `decode()`
- `len()` 对字符串和字节的区别
- `%` 格式化
- `format()` 格式化
- f-string 格式化

---

# 1. 字符串

Python 使用 `str` 表示字符串。

字符串可以使用单引号：

```python
s1 = 'hello'
```

也可以使用双引号：

```python
s2 = "hello"
```

两种方式都可以表示普通字符串。

```python
print(type("hello"))
```

结果：

```text
<class 'str'>
```

---

# 2. 转义字符

字符串中有一些字符具有特殊作用，例如换行、制表符等。

Python 使用反斜杠：

```text
\
```

表示转义。

常见转义字符：

| 转义字符 | 作用 |
| --- | --- |
| `\n` | 换行 |
| `\t` | 制表符 |
| `\\` | 表示一个反斜杠 |

---

## `\n` 换行

```python
print("hello\nworld")
```

输出：

```text
hello
world
```

这里的 `\n` 不会按照普通字符显示，而是表示换行。

---

## `\t` 制表符

```python
print("hello\tworld")
```

输出效果类似：

```text
hello	world
```

`\t` 表示制表符（Tab）。

---

## `\\` 表示反斜杠

由于 `\` 本身用于表示转义，因此如果字符串中真的需要一个反斜杠，可以写：

```python
print("hello\\world")
```

输出：

```text
hello\world
```

可以理解为：

```text
\\
↓
\
```

---

# 3. 原始字符串 `r"..."`

如果不希望 Python 对字符串中的反斜杠进行普通的转义处理，可以在字符串前添加：

```text
r
```

例如：

```python
print(r"hello\nworld")
```

输出：

```text
hello\nworld
```

这里：

```text
\n
```

没有被解释成换行，而是按照字符串中的字符显示出来。

对比：

```python
print("hello\nworld")
```

输出：

```text
hello
world
```

而：

```python
print(r"hello\nworld")
```

输出：

```text
hello\nworld
```

原始字符串在处理包含大量反斜杠的内容时比较方便，例如某些 Windows 路径和正则表达式。

例如：

```python
path = r"C:\Users\name"
```

相比：

```python
path = "C:\\Users\\name"
```

更加直观。

---

# 4. 多行字符串

如果字符串本身包含多行内容，可以使用三个单引号：

```python
'''
...
'''
```

例如：

```python
print('''第一行
第二行
第三行''')
```

输出：

```text
第一行
第二行
第三行
```

也可以使用三个双引号：

```python
"""
...
"""
```

例如：

```python
text = """第一行
第二行
第三行"""
```

因此：

```text
'''...'''
```

和：

```text
"""..."""
```

都可以用于表示多行字符串。

---

# 5. 字符串是不可变对象

Python 中的字符串属于**不可变对象（immutable object）**。

例如：

```python
s = "hello"
```

不能直接修改其中某个字符：

```python
s[0] = 'H'
```

会出现：

```text
TypeError: 'str' object does not support item assignment
```

也就是说，字符串创建之后，不能直接修改字符串内部的某一个字符。

如果需要得到修改后的字符串，本质上需要创建一个新的字符串。

可以简单记住：

```text
str → 不可变
```

这一点后面学习列表 `list` 时会形成明显对比。

---

# 6. 字符与编码

计算机底层最终存储和处理的是二进制数据，而我们看到的是：

```text
A
B
中
文
你
好
```

这样的字符。

因此需要建立一种规则，把：

```text
字符
```

转换成：

```text
数字
```

再进一步转换为计算机能够存储和传输的字节。

这个过程涉及**字符编码**。

可以先建立一个整体认识：

```text
字符
 ↓
Unicode 码点
 ↓
按照 UTF-8 等编码规则进行编码
 ↓
bytes 字节数据
 ↓
最终以二进制形式存储/传输
```

---

# 7. ASCII

ASCII 是较早的一套字符编码标准，主要包含：

- 英文字母
- 数字
- 常见英文符号
- 一些控制字符

例如字符：

```text
A
```

对应十进制数字：

```text
65
```

Python 中可以验证：

```python
print(ord('A'))
```

输出：

```text
65
```

ASCII 能表示的字符范围有限，无法直接表示大量其他语言的字符，例如中文。

---

# 8. Unicode

不同国家和语言拥有大量不同字符，如果每种语言都使用完全独立的编码方式，字符处理会非常复杂。

Unicode 的目标是：

> 为各种字符分配统一的编号。

这个编号通常称为：

```text
Unicode 码点（Code Point）
```

例如：

```text
A → 65
中 → 20013
```

Python 3 的 `str` 用于表示 Unicode 文本，因此可以直接处理：

```python
"hello"
"你好"
"中文"
```

等字符串。

---

# 9. `ord()`：字符 → Unicode 码点

Python 内置的：

```python
ord()
```

可以得到一个字符对应的 Unicode 码点。

例如：

```python
print(ord('A'))
```

结果：

```text
65
```

再例如：

```python
print(ord('中'))
```

结果：

```text
20013
```

因此：

```text
ord('A')   → 65
ord('中')  → 20013
```

可以简单记成：

```text
字符
 ↓ ord()
Unicode 码点
```

---

# 10. `chr()`：Unicode 码点 → 字符

`chr()` 的作用与 `ord()` 相反。

例如：

```python
print(chr(65))
```

输出：

```text
A
```

再例如：

```python
print(chr(20013))
```

输出：

```text
中
```

因此：

```text
Unicode 码点
 ↓ chr()
字符
```

`ord()` 和 `chr()` 是一组相反的转换：

```text
字符 ──ord()──> Unicode 码点

字符 <──chr()── Unicode 码点
```

例如：

```text
'A' ──ord()──> 65

'A' <──chr()── 65
```

---

# 11. Unicode 与 UTF-8 的区别

Unicode 和 UTF-8 不是完全相同的概念。

可以先简单理解为：

```text
Unicode
↓
规定“每个字符对应什么编号”
```

而：

```text
UTF-8
↓
规定“这些字符应该如何编码成字节”
```

例如：

```text
中
```

拥有自己的 Unicode 码点。

当这个字符需要保存到文件或通过网络传输时，可以使用 UTF-8 将它转换为对应的字节数据。

因此：

```text
字符
 ↓
Unicode 码点
 ↓
UTF-8 编码
 ↓
字节
```

---

# 12. `str` 和 `bytes`

Python 中需要区分两个概念：

```text
str
bytes
```

## `str`

表示文本字符串：

```python
text = "中文"
```

类型：

```python
print(type(text))
```

结果：

```text
<class 'str'>
```

---

## `bytes`

表示字节数据。

例如：

```python
b'ABC'
```

类型是：

```text
bytes
```

`bytes` 前面通常可以看到：

```text
b
```

例如：

```python
b'ABC'
```

与：

```python
'ABC'
```

并不是同一种类型。

一个表示字节数据，一个表示字符串文本。

---

# 13. `encode()`：字符串 → 字节

`encode()` 用于把：

```text
str
```

编码成：

```text
bytes
```

例如：

```python
print('ABC'.encode('ascii'))
```

结果：

```text
b'ABC'
```

也可以使用 UTF-8：

```python
print('中文'.encode('utf-8'))
```

结果：

```text
b'\xe4\xb8\xad\xe6\x96\x87'
```

因此：

```text
str
 ↓ encode()
bytes
```

例如：

```text
"中文"
   ↓ encode("utf-8")
UTF-8 字节数据
```

---

# 14. `decode()`：字节 → 字符串

`decode()` 与 `encode()` 的方向相反。

它用于把：

```text
bytes
```

解码成：

```text
str
```

例如：

```python
data = b'\xe4\xb8\xad\xe6\x96\x87'

print(data.decode('utf-8'))
```

结果：

```text
中文
```

因此：

```text
bytes
 ↓ decode()
str
```

---

# 15. `encode()` 与 `decode()` 的关系

可以把整个过程总结成：

```text
          encode("utf-8")
str  ----------------------> bytes
"中文"                       UTF-8字节

          decode("utf-8")
str  <---------------------- bytes
"中文"                       UTF-8字节
```

也就是：

```text
字符串 → encode() → 字节

字节 → decode() → 字符串
```

编码和解码时需要使用匹配的编码方式，否则可能产生乱码或者解码错误。

---

# 16. ASCII 与中文

ASCII 能表示的字符范围有限，因此不能直接用 ASCII 编码中文。

例如：

```python
"ABC".encode("ascii")
```

可以正常执行：

```text
b'ABC'
```

但是：

```python
"中文".encode("ascii")
```

不能正常编码，会出现：

```text
UnicodeEncodeError
```

因为 ASCII 中不存在对应的中文字符。

处理中文文本时通常使用 UTF-8：

```python
"中文".encode("utf-8")
```

---

# 17. `len()` 与字符串

对字符串使用：

```python
len()
```

得到的是**字符数量**。

例如：

```python
print(len("ABC"))
```

结果：

```text
3
```

因为：

```text
A B C
1 2 3
```

再例如：

```python
print(len("中文"))
```

结果：

```text
2
```

因为字符串中有两个字符：

```text
中 文
1  2
```

---

# 18. `len()` 与字节

如果先把字符串编码成 `bytes`，再使用 `len()`，得到的是**字节数量**。

例如：

```python
print(len("ABC".encode("ascii")))
```

结果：

```text
3
```

而：

```python
print(len("中文".encode("utf-8")))
```

结果：

```text
6
```

在这个 UTF-8 示例中：

```text
中 → 3 字节
文 → 3 字节
```

所以：

```text
3 + 3 = 6 字节
```

因此要特别区分：

```python
len("中文")
```

结果：

```text
2
```

表示：

```text
2 个字符
```

而：

```python
len("中文".encode("utf-8"))
```

结果：

```text
6
```

表示：

```text
6 个字节
```

可以记成：

```text
len(str)   → 字符数
len(bytes) → 字节数
```

---

# 19. 字符串格式化

字符串格式化的作用是：

> 将变量、数据或表达式插入到字符串中。

这一节涉及三种方式：

```text
% 操作符
format()
f-string
```

---

# 20. `%` 格式化

较早的 Python 代码中经常可以看到 `%` 格式化。

例如：

```python
name = "Alice"
age = 25

print("Hello, %s. You are %d years old." % (name, age))
```

输出：

```text
Hello, Alice. You are 25 years old.
```

这里：

```text
%s
```

用于放入字符串。

```text
%d
```

用于放入整数。

例如：

```python
print("name = %s" % "Alice")
```

输出：

```text
name = Alice
```

这种写法在旧代码中仍然可能遇到，因此需要能够看懂。

---

# 21. `format()` 格式化

另一种字符串格式化方式是：

```python
format()
```

例如：

```python
print("Hello, {}. You are {} years old.".format("Bob", 30))
```

输出：

```text
Hello, Bob. You are 30 years old.
```

字符串中的：

```text
{}
```

相当于需要填入内容的位置。

后面的：

```python
.format("Bob", 30)
```

会依次将数据放入对应的 `{}`。

可以理解为：

```text
"Hello, {}. You are {} years old."
         ↑          ↑
        Bob         30
```

---

# 22. f-string

Python 3.6+ 支持 f-string。

基本格式：

```python
f"...{变量}..."
```

例如：

```python
name = "Charlie"
age = 35

print(f"Hello, {name}. You are {age} years old.")
```

输出：

```text
Hello, Charlie. You are 35 years old.
```

字符串前面的：

```text
f
```

表示这是一个格式化字符串。

其中：

```python
{name}
```

会取得变量 `name` 的值。

```python
{age}
```

会取得变量 `age` 的值。

---

# 23. f-string 中可以直接写表达式

f-string 的 `{}` 中不仅可以放变量，还可以直接放表达式。

例如：

```python
print(f"计算结果: {1 + 2 + 3}")
```

Python 会先计算：

```text
1 + 2 + 3
```

得到：

```text
6
```

最终输出：

```text
计算结果: 6
```

因此：

```python
f"{表达式}"
```

会先计算表达式，再将结果放入字符串。

---

# 24. f-string 格式控制

f-string 还可以控制数据的显示格式。

例如：

```python
print(f"保留两位小数: {3.14159:.2f}")
```

输出：

```text
保留两位小数: 3.14
```

这里：

```text
:.2f
```

表示：

```text
:
↓
开始指定格式

.2
↓
保留两位小数

f
↓
按照浮点数形式显示
```

因此：

```python
f"{3.14159:.2f}"
```

得到：

```text
3.14
```

类似地：

```python
print(f"{3.14159:.1f}")
```

得到：

```text
3.1
```

---

# 25. 三种字符串格式化方式对比

假设：

```python
name = "Tom"
```

### `%` 格式化

```python
print("Hello, %s" % name)
```

### `format()`

```python
print("Hello, {}".format(name))
```

### f-string

```python
print(f"Hello, {name}")
```

三种方式都可以完成字符串格式化。

其中 f-string 写法通常更加直观：

```python
name = "Tom"
age = 20

print(f"{name} is {age} years old.")
```

而 `%` 和 `format()` 在已有 Python 代码中仍然可能遇到，因此需要能够识别和理解。

---

# 26. Python 3 中的字符串编码

Python 3 中：

```text
str → Unicode 文本
```

因此可以直接创建包含中文的字符串：

```python
name = "中文"
```

当文本需要保存到文件、通过网络传输或者与字节数据进行交互时，才通常需要考虑：

```text
str ↔ bytes
```

之间的编码和解码。

常见过程：

```text
程序中的文本
      ↓
     str
      ↓
encode("utf-8")
      ↓
    bytes
      ↓
文件 / 网络 / 二进制数据
```

读取回来后：

```text
文件 / 网络 / 二进制数据
      ↓
    bytes
      ↓
decode("utf-8")
      ↓
     str
      ↓
程序中的文本
```

---

# 🧠 本节重点总结

## 字符串

```python
"hello"
'hello'
```

类型：

```text
str
```

---

## 转义字符

```text
\n  → 换行
\t  → 制表符
\\  → 反斜杠
```

---

## 原始字符串

```python
r"hello\nworld"
```

其中的 `\n` 不按照普通换行转义处理。

---

## 多行字符串

```python
'''第一行
第二行
第三行'''
```

或者：

```python
"""第一行
第二行
第三行"""
```

---

## 字符串不可变

```python
s = "hello"
s[0] = "H"     # 错误
```

`str` 属于不可变对象。

---

## ASCII、Unicode 和 UTF-8

可以先建立如下关系：

```text
ASCII
→ 较早的字符编码标准，主要覆盖基础英文字符

Unicode
→ 为各种字符分配统一的码点

UTF-8
→ Unicode 的一种常见编码方式，用于把文本编码成字节
```

---

## `ord()`

```text
字符 → Unicode 码点
```

例如：

```python
ord("A")    # 65
ord("中")   # 20013
```

---

## `chr()`

```text
Unicode 码点 → 字符
```

例如：

```python
chr(65)       # A
chr(20013)    # 中
```

---

## `encode()`

```text
str → bytes
```

例如：

```python
"中文".encode("utf-8")
```

---

## `decode()`

```text
bytes → str
```

例如：

```python
data.decode("utf-8")
```

---

## `len()`

```text
len(str)   → 字符数量
len(bytes) → 字节数量
```

例如：

```python
len("中文")                   # 2
len("中文".encode("utf-8"))   # 6
```

---

## 三种字符串格式化方式

```python
# % 格式化
"Hello, %s" % name

# format()
"Hello, {}".format(name)

# f-string
f"Hello, {name}"
```

实际编写新代码时可以重点掌握 f-string，同时能够看懂前两种写法。

---

## f-string 中使用表达式

```python
f"{1 + 2 + 3}"
```

结果：

```text
6
```

---

## f-string 控制小数位数

```python
f"{3.14159:.2f}"
```

结果：

```text
3.14
```

---

# 🔗 编码转换关系

这一部分最容易混淆，可以统一记成：

```text
                   ord()
        字符 ───────────────→ Unicode 码点
         ↑                       │
         └──────── chr() ────────┘


                  encode()
        str ───────────────────→ bytes
         ↑                         │
         └────── decode() ─────────┘
```

注意这是**两组不同的转换**：

```text
ord() / chr()
```

解决的是：

```text
字符 ↔ Unicode 码点
```

而：

```text
encode() / decode()
```

解决的是：

```text
字符串 ↔ 字节
```

---

# ✅ 本节掌握

完成这一部分后，需要能够理解和使用：

- Python 字符串 `str`
- `\n`、`\t`、`\\` 等转义字符
- `r"..."` 原始字符串
- `'''...'''` 和 `"""..."""` 多行字符串
- 字符串为什么是不可变对象
- ASCII、Unicode、UTF-8 的基本区别
- Unicode 码点的含义
- 使用 `ord()` 将字符转换成 Unicode 码点
- 使用 `chr()` 将 Unicode 码点转换成字符
- `str` 和 `bytes` 的区别
- 使用 `encode()` 将字符串编码成字节
- 使用 `decode()` 将字节解码成字符串
- `len(str)` 和 `len(bytes)` 的区别
- `%` 字符串格式化的基本写法
- `format()` 的基本写法
- f-string 的基本写法
- 在 f-string 中使用变量和表达式
- 使用 `:.2f` 等格式控制浮点数显示