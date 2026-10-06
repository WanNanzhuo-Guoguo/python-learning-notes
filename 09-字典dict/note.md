# 09 - 字典 Dict

## 📌 本节知识点

- 字典 `dict` 的基本概念
- 字典的创建与访问
- 键值对 `key: value`
- 字典元素的添加和修改
- 判断 key 是否存在
- `get()` 安全获取数据
- `pop()` 删除键值对
- 字典的多种遍历方式
- `keys()`、`values()`、`items()`
- dict 的 key 类型要求
- 字典的哈希表原理
- 字典的插入顺序
- `setdefault()` 方法
- 字典推导式

---

# 1. 什么是字典

字典（Dictionary，简称 `dict`）是一种按照：

```text
key → value
```

形式保存数据的数据结构。

也就是：

```text
键 → 值
```

例如保存学生成绩：

```python
scores = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
```

其中：

```text
'Michael' → key
95        → value

'Bob'     → key
75        → value

'Tracy'   → key
85        → value
```

每一个：

```python
key: value
```

称为一个**键值对**。

字典的核心特点就是：

> 通过 `key` 查找对应的 `value`。

---

# 2. 创建字典

字典使用：

```python
{}
```

创建。

基本格式：

```python
字典名 = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
```

也可以写成一行：

```python
scores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
```

输出：

```python
print(scores)
```

结果：

```text
{'Michael': 95, 'Bob': 75, 'Tracy': 85}
```

创建空字典：

```python
d = {}
```

---

# 3. 通过 key 访问 value

字典不是通过数字下标访问数据，而是通过：

```python
字典[key]
```

获取对应的 value。

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

print(scores['Michael'])
```

输出：

```text
95
```

可以理解为：

```text
scores
   ↓
找到 key = 'Michael'
   ↓
取得对应 value
   ↓
95
```

所以：

```python
scores['Michael']
```

就是根据 `'Michael'` 这个 key 查找对应的成绩。:chatgpt-content-reference{index="3"}

---

# 4. key 不存在时会发生什么

如果使用：

```python
d[key]
```

访问一个不存在的 key，会产生：

```text
KeyError
```

例如：

```python
scores = {'Michael': 95}

print(scores['Tom'])
```

因为：

```text
'Tom'
```

并不存在于 `scores` 中，所以会报错。

因此字典访问常见的方式有：

```text
d[key]
   ↓
key 必须存在
   ↓
不存在 → KeyError
```

或者：

```text
d.get(key)
   ↓
key 不存在也不会报错
```

---

# 5. 添加新的键值对

向字典中添加数据，可以直接使用：

```python
d[key] = value
```

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

scores['Adam'] = 67
```

此时：

```python
print(scores)
```

结果：

```text
{
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85,
    'Adam': 67
}
```

因为原字典中不存在：

```text
'Adam'
```

所以：

```python
scores['Adam'] = 67
```

表示**新增一个键值对**。

---

# 6. 修改已有的 value

如果指定的 key 已经存在：

```python
d[key] = value
```

就不再是添加，而是**修改原来的 value**。

例如：

```python
scores['Bob'] = 80
```

原来：

```text
'Bob' → 75
```

修改后：

```text
'Bob' → 80
```

因此：

```python
scores['Adam'] = 67
```

和：

```python
scores['Bob'] = 80
```

虽然写法一样，但实际效果取决于 key 是否已经存在：

```text
d[key] = value
      │
      ↓
key 是否存在？
   /        \
 不存在      存在
   ↓          ↓
 添加        修改
```

:chatgpt-content-reference{index="4"}

---

# 7. 判断 key 是否存在

可以使用：

```python
key in dict
```

判断一个 key 是否存在于字典中。

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 80,
    'Tracy': 85
}

print('Michael' in scores)
print('Tom' in scores)
```

输出：

```text
True
False
```

也就是说：

```python
'Michael' in scores
```

判断的是：

```text
'Michael' 是否是 scores 的 key
```

而不是判断它是不是 value。

:chatgpt-content-reference{index="5"}

---

# 8. get() 安全获取 value

除了：

```python
d[key]
```

还可以使用：

```python
d.get(key)
```

获取 value。

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 80
}

print(scores.get('Michael'))
```

输出：

```text
95
```

两者在 key 存在时效果类似：

```python
scores['Michael']
```

和：

```python
scores.get('Michael')
```

都可以得到：

```text
95
```

但是 key 不存在时，两者的行为不同。

---

# 9. get() 与直接访问的区别

如果执行：

```python
scores['Tom']
```

而 `'Tom'` 不存在：

```text
KeyError
```

但是：

```python
scores.get('Tom')
```

会返回：

```text
None
```

不会报错。

例如：

```python
print(scores.get('Tom'))
```

输出：

```text
None
```

因此：

| 写法 | key 存在 | key 不存在 |
|---|---|---|
| `d[key]` | 返回 value | `KeyError` |
| `d.get(key)` | 返回 value | `None` |

所以当不能确定 key 是否存在时，`get()` 是一种更安全的获取方式。

---

# 10. get() 设置默认值

`get()` 还可以指定：

```text
key 不存在时返回什么
```

语法：

```python
d.get(key, default)
```

例如：

```python
print(scores.get('Tom', -1))
```

因为 `'Tom'` 不存在，所以返回：

```text
-1
```

因此：

```python
scores.get('Tom')
```

结果：

```text
None
```

而：

```python
scores.get('Tom', -1)
```

结果：

```text
-1
```

执行逻辑：

```text
d.get(key, default)
        │
        ↓
    key 存在？
     /     \
   是       否
   ↓         ↓
返回 value  返回 default
```

:chatgpt-content-reference{index="6"}

---

# 11. 删除键值对

可以使用：

```python
pop()
```

删除指定 key 对应的键值对。

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 80,
    'Tracy': 85,
    'Adam': 67
}

scores.pop('Adam')
```

执行后：

```python
print(scores)
```

结果：

```text
{'Michael': 95, 'Bob': 80, 'Tracy': 85}
```

也就是：

```text
删除前

'Adam' → 67

      ↓

scores.pop('Adam')

      ↓

删除后

字典中不再存在 'Adam'
```

:chatgpt-content-reference{index="7"}

---

# 12. 字典的增删改查总结

字典最基本的操作可以整理成：

| 操作 | 写法 |
|---|---|
| 创建 | `d = {'name': 'Tom'}` |
| 空字典 | `d = {}` |
| 查询 | `d[key]` |
| 安全查询 | `d.get(key)` |
| 添加 | `d[new_key] = value` |
| 修改 | `d[old_key] = new_value` |
| 删除 | `d.pop(key)` |
| 判断 key | `key in d` |

核心可以记成：

```text
增 → d[key] = value
删 → d.pop(key)
改 → d[key] = value
查 → d[key] / d.get(key)
```

---

# 13. 遍历字典

字典也可以使用 `for` 循环遍历。

例如：

```python
scores = {
    'Michael': 95,
    'Bob': 80,
    'Tracy': 85
}

for key in scores:
    print(key)
```

输出：

```text
Michael
Bob
Tracy
```

直接写：

```python
for key in scores:
```

默认遍历的是：

```text
key
```

因此如果还需要 value，可以通过：

```python
scores[key]
```

获取：

```python
for key in scores:
    print(f"{key}: {scores[key]}")
```

输出：

```text
Michael: 95
Bob: 80
Tracy: 85
```

:chatgpt-content-reference{index="8"}

---

# 14. items() 同时遍历 key 和 value

如果希望同时获得：

```text
key + value
```

可以使用：

```python
items()
```

例如：

```python
for key, value in scores.items():
    print(f"{key} => {value}")
```

输出：

```text
Michael => 95
Bob => 80
Tracy => 85
```

可以理解为：

```text
scores.items()
      ↓
得到每一个键值对
      ↓
(key, value)
      ↓
分别赋值给
key 和 value
```

因此：

```python
for key, value in scores.items():
```

是遍历字典时非常常见的写法。:chatgpt-content-reference{index="9"}

---

# 15. keys() 获取所有 key

使用：

```python
d.keys()
```

可以获得字典中的所有 key。

例如：

```python
print(scores.keys())
```

如果希望转换成列表：

```python
print(list(scores.keys()))
```

结果：

```text
['Michael', 'Bob', 'Tracy']
```

---

# 16. values() 获取所有 value

使用：

```python
d.values()
```

可以获得所有 value。

例如：

```python
print(list(scores.values()))
```

结果：

```text
[95, 80, 85]
```

因此：

```text
keys()   → key

values() → value

items()  → key + value
```

:chatgpt-content-reference{index="10"}

---

# 17. 字典的三种主要遍历方式

## 只遍历 key

```python
for key in scores:
    print(key)
```

也可以：

```python
for key in scores.keys():
    print(key)
```

---

## 只遍历 value

```python
for value in scores.values():
    print(value)
```

---

## 同时遍历 key 和 value

```python
for key, value in scores.items():
    print(key, value)
```

整理成表格：

| 方法 | 获取内容 |
|---|---|
| `for key in d` | key |
| `d.keys()` | 所有 key |
| `d.values()` | 所有 value |
| `d.items()` | key 和 value |

---

# 18. dict 的 key 必须满足一定条件

字典的 key 不能随意使用所有类型。

例如：

```python
d = {
    'name': 'Tom',
    1: 'one'
}
```

字符串和整数都可以作为 key。

tuple 在其中元素满足要求时也可以作为 key：

```python
d = {
    (1, 2): 'tuple_key'
}

print(d)
```

输出：

```text
{(1, 2): 'tuple_key'}
```

但是 list 不能作为 key：

```python
d = {
    [1, 2]: 'list_key'
}
```

会产生：

```text
TypeError: unhashable type: 'list'
```

在当前阶段可以先记住：

```text
常见可以作为 key
├── str
├── int
└── tuple（内部元素也需要满足要求）

不能作为 key
└── list
```

:chatgpt-content-reference{index="11"}

---

# 19. 为什么 list 不能作为 key

字典底层使用：

```text
哈希表 Hash Table
```

字典需要根据 key 计算对应的哈希值，从而确定数据存放和查找的位置。

因此 key 必须能够保持稳定。

而 list 是：

```text
可变对象
```

例如：

```python
a = [1, 2]

a.append(3)
```

内容可以从：

```text
[1, 2]
```

变成：

```text
[1, 2, 3]
```

因此 list 不能直接作为字典的 key。

可以简单理解为：

```text
dict 的 key
    ↓
需要用于哈希定位
    ↓
key 需要满足可哈希要求
    ↓
常见不可变类型可以
    ↓
list 这种可变类型不可以
```

---

# 20. dict 为什么查找很快

字典底层使用的是：

```text
Hash Table
哈希表
```

普通顺序查找可以理解为：

```text
第 1 个
 ↓
不是

第 2 个
 ↓
不是

第 3 个
 ↓
找到
```

而字典会根据：

```text
key
 ↓
哈希计算
 ↓
定位到对应位置
 ↓
取得 value
```

因此字典非常适合：

```text
通过一个唯一的 key
快速找到对应 value
```

平均情况下，字典的查找、插入等操作可以达到接近：

```text
O(1)
```

的时间复杂度。

不过这种高效查找通常需要更多内存空间，因此可以理解为一种：

```text
空间换时间
```

的设计。

:chatgpt-content-reference{index="12"}

---

# 21. 字典会保留插入顺序

在现代 Python 中，字典会按照元素的**插入顺序**保存键值对。

例如：

```python
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)
```

结果：

```text
{'a': 1, 'b': 2, 'c': 3}
```

遍历时：

```python
for key in d:
    print(key)
```

会按照插入顺序得到：

```text
a
b
c
```

Python 3.7+ 正式保证 dict 保留插入顺序。:chatgpt-content-reference{index="13"}

---

# 22. setdefault()

`setdefault()` 可以理解为：

> 获取某个 key 的 value，如果 key 不存在，就创建这个 key。

基本形式：

```python
d.setdefault(key, default)
```

例如：

```python
scores = {
    'Michael': 95
}

scores.setdefault('Bob', 80)

print(scores)
```

结果：

```text
{'Michael': 95, 'Bob': 80}
```

因为：

```text
'Bob'
```

原来不存在，所以：

```python
'Bob': 80
```

被加入字典。

如果 key 已经存在：

```python
scores.setdefault('Michael', 100)
```

原来的：

```text
'Michael': 95
```

不会被修改成 `100`。

---

# 23. get() 和 setdefault() 的区别

两者都可以处理：

```text
key 不存在
```

的情况，但是行为不同。

例如：

```python
d.get('Tom', 0)
```

如果 `'Tom'` 不存在：

```text
返回 0
```

但是不会修改字典。

而：

```python
d.setdefault('Tom', 0)
```

如果 `'Tom'` 不存在：

```text
返回 0
+
把 'Tom': 0 加入字典
```

因此：

| 方法 | key 不存在时 | 是否修改字典 |
|---|---|---|
| `get(key, default)` | 返回 default | ❌ |
| `setdefault(key, default)` | 返回 default | ✅ 添加键值对 |

:chatgpt-content-reference{index="14"}

---

# 24. 字典推导式

和列表推导式类似，字典也可以使用推导式快速创建。

基本形式：

```python
{key表达式: value表达式 for 变量 in 可迭代对象}
```

例如：

```python
squares = {x: x * x for x in range(1, 6)}

print(squares)
```

结果：

```text
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

执行逻辑：

```text
x = 1 → 1:1
x = 2 → 2:4
x = 3 → 3:9
x = 4 → 4:16
x = 5 → 5:25
```

最终组合成一个字典。

常见形式：

```python
{k: v for k, v in pairs}
```

可以用于根据已有数据快速构造新的字典。:chatgpt-content-reference{index="15"}

---

# 25. 字典操作整体关系

```text
                         dict
                          │
                    key → value
                          │
       ┌──────────────┬───┴───────────┐
       ↓              ↓               ↓
      创建           访问            修改
       │              │               │
{key: value}        d[key]        d[key] = value
       │              │
       │              ├── key 存在 → value
       │              └── 不存在 → KeyError
       │
       │            d.get(key)
       │              │
       │              └── 不存在 → None / default
       │
       ├──────────── 删除
       │              │
       │          d.pop(key)
       │
       └──────────── 判断
                      │
                  key in d
```

遍历：

```text
dict
 │
 ├── d.keys()   → key
 │
 ├── d.values() → value
 │
 └── d.items()  → key + value
```

---

# 26. 常用写法总结

## 创建字典

```python
scores = {
    'Michael': 95,
    'Bob': 80
}
```

## 创建空字典

```python
d = {}
```

## 获取 value

```python
scores['Michael']
```

## 安全获取

```python
scores.get('Michael')
```

## 设置默认返回值

```python
scores.get('Tom', -1)
```

## 添加数据

```python
scores['Adam'] = 67
```

## 修改数据

```python
scores['Bob'] = 90
```

## 判断 key

```python
'Bob' in scores
```

## 删除

```python
scores.pop('Bob')
```

## 遍历 key

```python
for key in scores:
    print(key)
```

## 遍历 value

```python
for value in scores.values():
    print(value)
```

## 遍历 key 和 value

```python
for key, value in scores.items():
    print(key, value)
```

---

# 🧠 本节重点总结

| 知识点 | 核心含义 |
|---|---|
| `dict` | 使用 `key: value` 保存数据 |
| `{}` | 创建空字典 |
| `{key: value}` | 创建包含数据的字典 |
| `d[key]` | 根据 key 获取 value |
| `d.get(key)` | 安全获取，key 不存在返回 `None` |
| `d.get(key, default)` | key 不存在返回指定默认值 |
| `d[key] = value` | 添加或修改键值对 |
| `key in d` | 判断 key 是否存在 |
| `d.pop(key)` | 删除指定键值对 |
| `d.keys()` | 获取所有 key |
| `d.values()` | 获取所有 value |
| `d.items()` | 获取所有 key-value |
| `setdefault()` | key 不存在时添加默认键值对 |
| 字典推导式 | 快速构建字典 |
| key | 必须满足可哈希要求 |
| 哈希表 | dict 高效查找的基础 |
| 插入顺序 | Python 3.7+ 保证保留 |

---

# 🔗 字典整体关系

```text
                  字典 dict
                     │
                  key:value
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
       增删          查改          遍历
        │            │            │
 d[key] = value    d[key]       keys()
 d.pop(key)        get()        values()
                  key in d      items()
                     │
                     ↓
                  key 要求
                     │
              必须满足可哈希要求
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
     str / int / tuple        list
          ↓                     ↓
       常见可用               不可用

                  dict 底层
                     │
                  哈希表
                     │
                     ↓
              快速根据 key 查找
                     │
                  平均 O(1)
```

---

# ✅ 本节掌握

学习完本节后，需要能够：

- 理解字典使用 `key: value` 保存数据
- 使用 `{}` 创建空字典
- 创建包含多个键值对的字典
- 使用 `d[key]` 获取对应 value
- 理解不存在的 key 会导致 `KeyError`
- 使用 `get()` 安全获取 value
- 使用 `get(key, default)` 设置默认返回值
- 使用 `d[key] = value` 添加和修改数据
- 使用 `key in d` 判断 key 是否存在
- 使用 `pop()` 删除键值对
- 使用 `for` 遍历字典的 key
- 使用 `keys()`、`values()` 和 `items()`
- 理解字典 key 需要满足可哈希要求
- 知道 list 不能直接作为 dict 的 key
- 理解 dict 底层使用哈希表进行快速查找
- 知道字典高效查找与额外内存开销之间的关系
- 知道 Python 3.7+ 的 dict 保留插入顺序
- 理解 `get()` 和 `setdefault()` 的区别
- 了解字典推导式的基本写法