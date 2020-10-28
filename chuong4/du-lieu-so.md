# Bài 21. Dữ liệu kiểu số

Python có 2 loại dữ liệu số học gồm số nguyên, số thực \(dấu phẩy động\) và số phức. Cùng xem qua các ví dụ dưới đây về các kiểu dữ liệu số:

```python
a = 5
print(type(a))
print(type(5.0))
c = 5 + 3j
print(c + 3)
print(isinstance(c, complex))
 
''' Output:
    <class 'int'>
    <class 'float'>
    (8+3j)
    True 
'''    
```

Số nguyên và số thực được phân biệt bằng cách có hoặc không có dấu thập phân. Ví dụ: 5 là số nguyên trong khi 5.0 là số thực. Số phức được viết dưới dạng x + yj, trong đó x là phần thực và y là phần ảo.

Số nguyên trong Python có thể có độ dài bất kỳ, số thực chỉ giới hạn đến 15 chữ số thập phân.

Trong Python, chúng ta có thể biểu diễn số nhị phân \(cơ số 2\), hệ thập lục phân \(cơ số 16\) và hệ bát phân \(cơ số 8\) bằng cách đặt một tiền tố một cách thích hợp theo quy ước sau:

Binary:			'0b' hoặc '0B'  
Octal:			'0o' hoặc '0O'  
Hexadecimal:	'0x' hoặc '0X'

```python
print(0b1101011)
print(0xFB + 0b10)
print(0o15)

''' Output:
    107
    253
    13
'''
```

## Chuyển đổi kiểu dữ liệu

Python tự động chuyển kiểu int sang float khi thực hiện các phép tính giữa số nguyên và thực. Ví dụ:

```python
a = 1
b = 2.0
c = a + b
print(c)

# output: 3.0 
```

Ép kiểu dữ liệu bằng cách khai báo kiểu. Ví dụ:

```python
a = int(2.3)
b = int(-2.8)
c = float(5)
d = complex('3+5j')
print(a)
print(b)
print(c)
print(d)

''' output:
    2
    -2
    5.0
    (3+5j)
'''
```

## Số thập phân

Một điều cần chú ý đối với kiểu dữ liệu float trong Python là 1.1 + 2.2 không bằng 3.3! 

```python
print(1.1+2.2==3.3)

#output: False
```

Nguyên nhân là bởi số thực được lưu trữ trong máy tính dưới dạng phân số nhị phân \(0 và 1\). Vì vậy hầy hết các phân số không thể biểu diễn chính xác trong máy tính.

Ví dụ, ta không thể biểu diễn chính xác phân số 1/3 bằng số thập phân vì nó sẽ là 0,33333333 ... \(dài vô hạn\). Tương tự, 0.1 cũng chỉ là biểu diễn gần dúng chứ không hoàn toàn đúng. Đó là lý do vì sáo 1.1+2.2 không = 3.3

Để biểu diễn và tính toán số thực một cách bình thường \(như trong toán học\) thì ta sử dụng module decimal

Ví dụ:

```python
from decimal import Decimal as d

print(d('1.1') + d('2.2'))
print(d('1.0') * d('2.5'))

''' output:
    3.3
    2.50
'''
```

**Khi nào cần dùng decimal thay cho float?**

* Khi ta thực hiện các ứng dụng tài chính cần biểu diễn số thập phân chính xác. 
* Khi ta muốn triển khai khái niệm về số thập phân một cách chính xác.

## Phân số

Python hỗ trợ module fractions để xử lý phân số. Có nhiều cách để biểu diễn phân số, ví dụ như sau:

```python
from fractions import Fraction as F

print(F(5))
print(F(1,3))
print(F('1.1'))

''' Output:
    5
    1/3
    11/10
'''
```

Phân số được biểu diễn bởi số nguyên cho cả tử và mẫu hoặc có thể biểu diễn bằng string. Không thể dùng số thực để biểu diễn phân số vì sẽ cho kết quả không đúng. Ví dụ:

```python
from fractions import Fraction as F

print(F(1.3))
print(F('1.3'))

''' Output:
    5854679515581645/4503599627370496
    13/10
'''
```

Dữ liệu kiểu phân số có thể dùng tất cả các toán tử cơ bản. Ví dụ:

```python
from fractions import Fraction as F

print(F(1, 3) + F(1, 3))
print(F(1, 3) * F(1, 3))
print(1 / F(5, 6))
print(F(-3, 10) > 0)
print(F(-3, 10) < 0)

''' Output:
    2/3
    1/9
    6/5
    False
    True
'''
```

## Toán học trong Python

Python cung cấp module như math và random để thực hiện các phép toán khác nhau như lượng giác, logarit, xác suất và thống kê, v.v

```python
import math as m

print(m.pi)
print(m.cos(m.pi))
print(m.exp(10))
print(m.log10(1000))
print(m.sinh(1))
print(m.factorial(6))

''' output:
    3.141592653589793
    -1.0
    22026.465794806718
    3.0
    1.1752011936438014
    720
'''
```

Xem thêm về các hàm toán học tại đây: [math](https://www.programiz.com/python-programming/modules/math)

```python
import random as rd

print(rd.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

print(rd.choice(x))
rd.shuffle(x)
print(x)
print(rd.random())

# Output: Mỗi lần run sẽ ra một kết quả ngẫu nhiên khác nhau
```

