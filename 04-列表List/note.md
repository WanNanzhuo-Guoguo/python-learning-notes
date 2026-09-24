# 04 - 列表 List

## 📌 本节知识点

这一节主要学习 Python 中的列表 `list`，包括：

- 列表的基本概念
- 列表的创建
- 空列表
- 使用 `len()` 获取列表长度
- 正索引和负索引
- 索引越界
- 使用 `append()` 追加元素
- 使用 `insert()` 插入元素
- 使用 `pop()` 删除元素
- 使用 `remove()` 按值删除元素
- 修改列表中的元素
- 使用 `in` 判断元素是否存在
- 列表中存储不同类型的数据
- 嵌套列表
- 使用 `sort()` 对列表排序
- `sort()` 与 `sorted()` 的区别
- 列表的拼接和重复

---

# 1. 列表 `list`

Python 使用 `list` 表示列表。

列表可以一次保存多个元素，例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']
```

打印列表：

```python
print(classmates)
```

输出：

```text
['Michael', 'Bob', 'Tracy']
```

查看类型：

```python
print(type(classmates))
```

结果：

```text
<class 'list'>
```

列表具有几个比较重要的特点：

```text
有序
可变
支持索引访问
可以保存不同类型的数据
可以嵌套其他列表
```

其中最重要的是：

```text
list → 有序、可变
```

这里的**可变**表示列表创建之后，其中的元素仍然可以进行增加、删除和修改。

---

# 2. 创建列表

列表使用：

```text
[]
```

表示。

元素之间使用逗号：

```text
,
```

分隔。

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']
```

也可以创建数字列表：

```python
nums = [1, 2, 3, 4, 5]
```

或者：

```python
scores = [95, 87, 100]
```

基本形式可以写成：

```python
列表名 = [元素1, 元素2, 元素3, ...]
```

---

# 3. 空列表

如果列表中暂时没有任何元素，可以创建一个空列表：

```python
empty = []
```

查看长度：

```python
print(len(empty))
```

结果：

```text
0
```

因此：

```python
[]
```

表示一个没有任何元素的列表。

---

# 4. `len()` 获取列表长度

使用：

```python
len()
```

可以获取列表中元素的数量。

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']

print(len(classmates))
```

输出：

```text
3
```

因为列表中一共有三个元素：

```text
Michael
Bob
Tracy
```

因此：

```text
len(list) → 列表中的元素数量
```

---

# 5. 列表索引

列表中的每个元素都有对应的位置，可以通过**索引**访问元素。

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']
```

可以理解为：

```text
索引        0          1        2
           ↓          ↓        ↓
元素    Michael      Bob      Tracy
```

访问第一个元素：

```python
print(classmates[0])
```

输出：

```text
Michael
```

访问第二个元素：

```python
print(classmates[1])
```

输出：

```text
Bob
```

因此需要注意：

```text
Python 的索引从 0 开始
```

也就是说：

```text
第 1 个元素 → 索引 0
第 2 个元素 → 索引 1
第 3 个元素 → 索引 2
```

---

# 6. 负索引

Python 除了可以从前往后访问列表，还可以从后往前访问。

负索引从：

```text
-1
```

开始。

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']

print(classmates[-1])
```

输出：

```text
Tracy
```

因为：

```text
-1 → 最后一个元素
```

继续向前：

```python
print(classmates[-2])
```

输出：

```text
Bob
```

整个列表的正负索引关系可以表示为：

```text
正索引       0          1        2
             ↓          ↓        ↓
元素      Michael      Bob      Tracy
             ↑          ↑        ↑
负索引      -3         -2       -1
```

因此可以记成：

```text
正索引 → 从左向右，从 0 开始
负索引 → 从右向左，从 -1 开始
```

---

# 7. 索引越界

列表索引不能超过列表实际存在的范围。

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']
```

这个列表只有三个元素，因此正索引只有：

```text
0
1
2
```

如果访问：

```python
classmates[3]
```

就会产生：

```text
IndexError
```

因为索引 `3` 对应的元素不存在。

对于长度为 `n` 的列表：

```text
正索引范围：

0 ~ n - 1
```

负索引范围：

```text
-n ~ -1
```

---

# 8. `append()`：末尾添加元素

如果需要向列表末尾添加一个元素，可以使用：

```python
append()
```

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']

classmates.append('Adam')

print(classmates)
```

输出：

```text
['Michael', 'Bob', 'Tracy', 'Adam']
```

可以理解为：

```text
原列表：

Michael → Bob → Tracy

             append('Adam')
                    ↓

Michael → Bob → Tracy → Adam
```

因此：

```python
list.append(x)
```

表示：

```text
在列表末尾添加元素 x
```

---

# 9. `insert()`：指定位置插入元素

如果需要在指定位置插入元素，可以使用：

```python
insert()
```

基本格式：

```python
list.insert(索引, 元素)
```

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy', 'Adam']

classmates.insert(1, 'Jack')

print(classmates)
```

输出：

```text
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

这里：

```python
insert(1, 'Jack')
```

表示：

```text
在索引 1 的位置插入 'Jack'
```

原来：

```text
0          1        2        3
Michael    Bob      Tracy    Adam
```

插入之后：

```text
0          1        2        3        4
Michael    Jack     Bob      Tracy    Adam
```

原来索引 `1` 以及后面的元素会依次向后移动。

---

# 10. `append()` 与 `insert()` 的区别

两者都可以向列表中增加元素。

区别是：

| 方法 | 作用 |
| --- | --- |
| `append(x)` | 在列表末尾添加元素 |
| `insert(i, x)` | 在指定索引 `i` 处插入元素 |

例如：

```python
L = [1, 2, 3]

L.append(4)
```

得到：

```text
[1, 2, 3, 4]
```

而：

```python
L = [1, 2, 3]

L.insert(1, 4)
```

得到：

```text
[1, 4, 2, 3]
```

---

# 11. `pop()`：删除末尾元素

使用：

```python
pop()
```

可以删除列表中的元素。

如果不指定索引：

```python
list.pop()
```

默认删除最后一个元素。

例如：

```python
classmates = ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

classmates.pop()

print(classmates)
```

输出：

```text
['Michael', 'Jack', 'Bob', 'Tracy']
```

这里删除的是：

```text
Adam
```

因此：

```text
pop() → 默认删除列表最后一个元素
```

---

# 12. `pop(i)`：删除指定位置元素

`pop()` 也可以指定索引。

基本格式：

```python
list.pop(i)
```

表示删除索引 `i` 对应的元素。

例如：

```python
classmates = ['Michael', 'Jack', 'Bob', 'Tracy']

classmates.pop(1)

print(classmates)
```

输出：

```text
['Michael', 'Bob', 'Tracy']
```

因为：

```text
索引 1 → Jack
```

所以 `'Jack'` 被删除。

可以总结为：

```python
L.pop()       # 删除最后一个元素

L.pop(i)      # 删除索引 i 对应的元素
```

---

# 13. `remove()`：按值删除元素

如果已经知道元素的值，而不是元素的索引，可以使用：

```python
remove()
```

例如：

```python
nums = [1, 2, 3, 2, 4]

nums.remove(2)

print(nums)
```

输出：

```text
[1, 3, 2, 4]
```

这里需要注意：

```text
remove() 删除第一个匹配的元素
```

原来的列表中存在两个 `2`：

```text
[1, 2, 3, 2, 4]
```

执行：

```python
nums.remove(2)
```

只会删除第一个 `2`。

---

# 14. `pop()` 与 `remove()` 的区别

两者都可以删除列表中的元素，但是删除方式不同。

| 方法 | 删除依据 |
| --- | --- |
| `pop()` | 删除最后一个元素 |
| `pop(i)` | 根据索引删除 |
| `remove(x)` | 根据元素的值删除 |

例如：

```python
L = ['A', 'B', 'C']
```

执行：

```python
L.pop(1)
```

表示：

```text
删除索引 1 的元素
```

也就是：

```text
B
```

而：

```python
L.remove('B')
```

表示：

```text
找到值为 'B' 的元素并删除
```

---

# 15. 修改列表元素

列表属于**可变对象**，因此可以直接修改指定位置的元素。

例如：

```python
classmates = ['Michael', 'Bob', 'Tracy']

classmates[1] = 'Sarah'

print(classmates)
```

输出：

```text
['Michael', 'Sarah', 'Tracy']
```

这里：

```python
classmates[1]
```

原来对应：

```text
Bob
```

执行：

```python
classmates[1] = 'Sarah'
```

之后就变成了：

```text
Sarah
```

因此修改列表元素的基本形式是：

```python
list[索引] = 新值
```

---

# 16. 列表是可变对象

前面学习字符串时：

```text
str → 不可变
```

例如字符串不能直接修改某一个字符：

```python
s = "hello"

s[0] = "H"       # 错误
```

但是列表可以：

```python
L = ['A', 'B', 'C']

L[0] = 'X'
```

结果：

```text
['X', 'B', 'C']
```

因此：

```text
str  → 不可变
list → 可变
```

这也是字符串和列表之间一个比较重要的区别。

---

# 17. `in`：判断元素是否存在

使用：

```python
in
```

可以判断某个元素是否存在于列表中。

例如：

```python
classmates = ['Michael', 'Sarah', 'Tracy']

print('Michael' in classmates)
```

输出：

```text
True
```

而：

```python
print('Tom' in classmates)
```

输出：

```text
False
```

因此：

```text
元素 in 列表
```

得到的是一个布尔值：

```text
存在   → True
不存在 → False
```

---

# 18. 列表可以存储不同类型的数据

Python 列表中的元素不要求必须是同一种数据类型。

例如：

```python
mixed = ['Apple', 123, True, None, [1, 2, 3]]

print(mixed)
```

输出：

```text
['Apple', 123, True, None, [1, 2, 3]]
```

这里同时包含：

```text
'Apple'      → 字符串 str
123          → 整数 int
True         → 布尔值 bool
None         → None
[1, 2, 3]    → 列表 list
```

因此 Python 列表中可以保存不同类型的对象。

可以简单理解为：

```text
list
 │
 ├── str
 ├── int
 ├── bool
 ├── None
 └── list
```

Python 列表中保存的是对对象的引用，因此这些引用可以指向不同类型的 Python 对象。

---

# 19. 嵌套列表

列表中的元素本身也可以是列表。

例如：

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

可以理解为：

```text
matrix
 │
 ├── [1, 2, 3]
 ├── [4, 5, 6]
 └── [7, 8, 9]
```

如果访问：

```python
matrix[1]
```

得到：

```text
[4, 5, 6]
```

如果继续访问：

```python
matrix[1][2]
```

得到：

```text
6
```

整个过程可以理解为：

```text
matrix[1]
    ↓
[4, 5, 6]
       ↓
      [2]
       ↓
       6
```

因此：

```python
matrix[1][2]
```

表示：

```text
先找到索引 1 对应的列表
再找到这个列表中索引 2 对应的元素
```

也就是：

```text
第 2 行，第 3 列
```

---

# 20. `sort()`：列表排序

列表可以使用：

```python
sort()
```

进行排序。

例如：

```python
nums = [3, 1, 4, 1, 5, 9]

nums.sort()

print(nums)
```

输出：

```text
[1, 1, 3, 4, 5, 9]
```

默认情况下按照升序排列。

可以理解为：

```text
原列表：

[3, 1, 4, 1, 5, 9]

        ↓ sort()

[1, 1, 3, 4, 5, 9]
```

---

# 21. `sort()` 是原地排序

`sort()` 一个比较重要的特点是：

```text
直接修改原来的列表
```

例如：

```python
nums = [3, 1, 2]

nums.sort()

print(nums)
```

输出：

```text
[1, 2, 3]
```

原来的：

```text
[3, 1, 2]
```

已经被修改。

另外，`sort()` 的返回值是：

```text
None
```

例如：

```python
nums = [3, 1, 2]

result = nums.sort()

print(result)
```

输出：

```text
None
```

所以不要写成：

```python
new_list = nums.sort()
```

然后认为 `new_list` 是排序后的列表。

实际上：

```text
new_list → None
```

---

# 22. `sorted()`：返回新的排序结果

除了 `sort()`，Python 还可以使用：

```python
sorted()
```

进行排序。

例如：

```python
nums = [3, 1, 2]

new_nums = sorted(nums)

print(nums)
print(new_nums)
```

输出：

```text
[3, 1, 2]
[1, 2, 3]
```

可以看到：

```text
nums
```

没有发生改变。

而：

```text
new_nums
```

保存了排序之后的新列表。

因此：

```text
             是否修改原列表       返回结果

sort()             是              None

sorted()           否              新列表
```

可以记成：

```python
L.sort()
```

表示：

```text
直接把 L 排好序
```

而：

```python
sorted(L)
```

表示：

```text
根据 L 创建一个排好序的新列表
```

---

# 23. 列表拼接 `+`

列表之间可以使用：

```text
+
```

进行拼接。

例如：

```python
a = [1, 2]
b = [3, 4]

print(a + b)
```

输出：

```text
[1, 2, 3, 4]
```

也就是：

```text
[1, 2] + [3, 4]

        ↓

[1, 2, 3, 4]
```

---

# 24. 列表重复 `*`

列表还可以使用：

```text
*
```

进行重复。

例如：

```python
nums = [0] * 5

print(nums)
```

输出：

```text
[0, 0, 0, 0, 0]
```

也就是：

```text
[0] * 5

   ↓

[0, 0, 0, 0, 0]
```

---

# 25. 列表常用操作对比

列表的基本操作可以统一整理为：

| 操作 | 写法 | 作用 |
| --- | --- | --- |
| 创建 | `L = [1, 2, 3]` | 创建列表 |
| 空列表 | `L = []` | 创建空列表 |
| 长度 | `len(L)` | 获取元素数量 |
| 访问 | `L[i]` | 根据索引访问元素 |
| 末尾添加 | `L.append(x)` | 在末尾添加元素 |
| 指定位置插入 | `L.insert(i, x)` | 在索引 `i` 处插入 |
| 删除末尾 | `L.pop()` | 删除最后一个元素 |
| 按索引删除 | `L.pop(i)` | 删除索引 `i` 的元素 |
| 按值删除 | `L.remove(x)` | 删除第一个值为 `x` 的元素 |
| 修改 | `L[i] = x` | 修改指定元素 |
| 判断存在 | `x in L` | 判断元素是否存在 |
| 原地排序 | `L.sort()` | 修改原列表进行排序 |
| 排序新列表 | `sorted(L)` | 返回新的排序列表 |
| 拼接 | `L1 + L2` | 拼接两个列表 |
| 重复 | `L * n` | 重复列表内容 |

---

# 🧠 本节重点总结

## 列表

列表使用：

```python
L = [1, 2, 3]
```

类型：

```text
list
```

最重要的特点：

```text
有序
可变
支持索引
```

---

## 正索引和负索引

```text
正索引       0       1       2
             ↓       ↓       ↓
列表        'A'     'B'     'C'
             ↑       ↑       ↑
负索引      -3      -2      -1
```

因此：

```python
L[0]      # 第一个元素

L[-1]     # 最后一个元素
```

---

## 添加元素

```python
L.append(x)
```

表示：

```text
在末尾添加 x
```

而：

```python
L.insert(i, x)
```

表示：

```text
在索引 i 的位置插入 x
```

---

## 删除元素

```python
L.pop()
```

删除：

```text
最后一个元素
```

```python
L.pop(i)
```

删除：

```text
索引 i 对应的元素
```

```python
L.remove(x)
```

删除：

```text
第一个值为 x 的元素
```

---

## 修改元素

```python
L[i] = new_value
```

表示修改索引 `i` 对应的元素。

因此：

```text
list → 可变对象
```

---

## 判断元素是否存在

```python
x in L
```

结果：

```text
存在   → True
不存在 → False
```

---

## 嵌套列表

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

访问：

```python
matrix[1][2]
```

结果：

```text
6
```

可以理解为：

```text
先找外层列表
再找内层列表中的元素
```

---

## `sort()` 和 `sorted()`

```python
L.sort()
```

表示：

```text
修改原列表
返回 None
```

而：

```python
sorted(L)
```

表示：

```text
原列表不变
返回新的排序列表
```

关系：

```text
L.sort()
   ↓
直接修改 L


sorted(L)
   ↓
返回新的排序列表
```

---

## 列表拼接和重复

拼接：

```python
[1, 2] + [3, 4]
```

结果：

```text
[1, 2, 3, 4]
```

重复：

```python
[0] * 5
```

结果：

```text
[0, 0, 0, 0, 0]
```

---

# 🔗 列表基本操作关系

列表的基本操作可以统一记成：

```text
                         list
                           │
          ┌────────────────┼────────────────┐
          │                │                │
         访问             修改             判断
          │                │                │
        L[i]            L[i] = x          x in L


                          增加
                           │
                ┌──────────┴──────────┐
                │                     │
            append(x)            insert(i, x)
                │                     │
             末尾添加             指定位置插入


                          删除
                           │
             ┌─────────────┼─────────────┐
             │             │             │
           pop()         pop(i)       remove(x)
             │             │             │
          删除末尾       按索引删除      按值删除
```

---

# ✅ 本节掌握

完成这一部分后，需要能够理解和使用：

- Python 列表 `list`
- 使用 `[]` 创建列表
- 使用 `[]` 创建空列表
- 使用 `len()` 获取列表长度
- 列表索引从 `0` 开始
- 使用负索引从列表末尾访问元素
- 索引越界会产生 `IndexError`
- 使用 `append()` 在列表末尾添加元素
- 使用 `insert()` 在指定位置插入元素
- 使用 `pop()` 删除最后一个元素
- 使用 `pop(i)` 根据索引删除元素
- 使用 `remove()` 根据值删除元素
- 使用 `L[i] = x` 修改列表元素
- 理解列表属于可变对象
- 使用 `in` 判断元素是否存在
- 理解列表可以保存不同类型的数据
- 理解嵌套列表
- 使用 `L[i][j]` 访问嵌套列表中的元素
- 使用 `sort()` 对原列表进行排序
- 理解 `sort()` 会修改原列表并返回 `None`
- 使用 `sorted()` 获得新的排序列表
- 理解 `sort()` 和 `sorted()` 的区别
- 使用 `+` 拼接列表
- 使用 `*` 重复列表