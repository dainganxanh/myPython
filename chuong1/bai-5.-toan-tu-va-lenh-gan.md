# Bài 5. Toán tử và lệnh gán

## 1. Toán tử số học

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| + | Cộng | x + y+ 2 |
| - | Trừ | x - y- 2 |
| \* | Nhân | x \* y |
| / | Chia | x / y |
| % | Lấy phần dư của phép chia \(mod\) | x % y |
| // | Lấy phần nguyên của phép chia \(div\) | x // y |
| \*\* | Lỹ thừa | x\*\*y \(xy\) |

Ví dụ:

```python
x = 19
print('x =',x)
y = 4
print('y =',y)
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x % y =',x%y)
print('x ** y =',x**y)
```

Output:

> x = 19  
> y = 4  
> x + y = 23  
> x - y = 15  
> x \* y = 76  
> x / y = 4.75  
> x // y = 4  
> x % y = 3  
> x \*\* y = 130321

## 2. Toán tử so sánh

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| &gt;  | Lớn hơn | x &gt; y |
| &lt;  | Nhỏ hơn | x &lt; y |
| == | Bằng | x == y |
| != | Khác | x != y |
| &gt;= | Lớn hơn hoặc bằng | x &gt;= y |
| &lt;= | Nhỏ hơn hoặc bằng | x &lt;= y |

Ví dụ:

```python
x = 10
y = 12
print('x > y is',x>y)
print('x < y is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)
```

Output:

> x &gt; y is False  
> x &lt; y is True  
> x == y is False  
> x != y is True  
> x &gt;= y is False  
> x &lt;= y is True

## 3. Toán tử logic

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| and | Và: True khi cả hai đều True | x and y |
| or | Hoặc: True nếu một trong hai là True | x or y |
| not | Không: True khi False | not x |

Ví dụ:

```python
x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)
```

Output:

> x and y is False  
> x or y is True  
> not x is False

## 4. Toán tử bitwise

Toán tử bitwise dùng để làm việc với các toán hạng nhị phân.

Ví dụ, với x = 10 \(0000 1010\) và y = 4 \(0000 0100\)

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| & | Bitwise AND | x & y |
| \| | Bitwise OR | x \| y |
| ~ | Bitwise NOT | ~x |
| ^ | Bitwise XOR | x ^ y |
| &gt;&gt;  | Bitwise dịch phải | x &gt;&gt; 2 \(dịch phải 2 bít\) |
| &lt;&lt;  | Bitwise dịch trái \(chuyển trái | x &lt;&lt; 2 \(dịch trái 2 bít\) |

```python
x = 10
print('x =',x)
y = 4
print('x',y)
print('x & y =',x&y)
print('x | y =',x|y)
print('~x =',~x)
print('x ^ y =',x^y)
print('x >> 2 =',x>>2)
print('x << 2 =',x<<2)
input()
```

Output:

> x = 10  
> x 4  
> x & y = 0  
> x \| y = 14  
> ~x = -11  
> x ^ y = 14  
> x &gt;&gt; 2 = 2  
> x &lt;&lt; 2 = 40

## 5. Toán tử gán

| Operator | Example | Equivalent to |
| :--- | :--- | :--- |
| = | x = 5 | x = 5 |
| += | x += 5 | x = x + 5 |
| -= | x -= 5 | x = x - 5 |
| \*= | x \*= 5 | x = x \* 5 |
| /= | x /= 5 | x = x / 5 |
| %= | x %= 5 | x = x % 5 |
| //= | x //= 5 | x = x // 5 |
| \*\*= | x \*\*= 5 | x = x \*\* 5 |
| &= | x &= 5 | x = x & 5 |
| \|= | x \|= 5 | x = x \| 5 |
| ^= | x ^= 5 | x = x ^ 5 |
| &gt;&gt;= | x &gt;&gt;= 5 | x = x &gt;&gt; 5 |
| &lt;&lt;= | x &lt;&lt;= 5 | x = x &lt;&lt; 5 |

