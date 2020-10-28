# Bài 19. Module

Một module \(đọc là mô-đun\) là một file chứa mã Python, ví dụ file vidumodule.py là một module và module này có tên là vidumodule \(tên module là tên file\).

Chúng ta sử dụng các module để chia nhỏ các chương trình lớn thành các tệp nhỏ để dễ quản lý và sắp xếp. Đồng thời sử dụng module cho phép ta dùng lại các hàm đã xây dựng mà không phải viết lại.

## **1. Tạo và sử dụng module**

**Bước 1.** Gõ nội dung dưới đây và lưu file với tên _**vidumodule.py**_ . Lưu ý: file _**vidumodule.py**_ được lưu cùng thư mục với file chương trình Python \(thường là file main.py\). 

```python
# Module vidu
def cong(a, b):
   """phép cộng 2 số """

   kq = a + b
   return kq
```

**Bước 2.** Sử dụng mudule vừa tạo

```python
import vidumodule

s = vidumodule.cong(4,5)
print(s)
```

Output: `9`

Chú thích:   
Câu lệnh dòng 1: Câu lệnh import để gọi \(nhập\) module có tên là vidumodule vào chương trình.  
Câu lệnh dòng 3: Sử dụng hàm cong\(\) đã được định nghĩa trong module vidumodule . 

## 2. Câu lệnh import

Câu lệnh import dùng để gọi \(nhập/nhúng\) module vào chương trình Python. Sau khi đã import ta có thể gọi hàm trong module theo cú pháp: tên module.tên hàm. 

Có 3 cách import module như sau:

### Lệnh import theo tên module

```python
import math
print("Căn bậc hai của 4 là: ", math.sqrt(4) )
```

Chương trình trên import module math sau đó gọi hàm sqrt\(\) đã được định nghĩa trong module math.

Output: `2.0`

###  Lệnh import đổi tên module

```python
import math as m
print("Căn bậc hai của 4 là: ", m.sqrt(4) )
```

### Câu lệnh import có chỉ định đối tượng

```python
from math import sqrt
print("Căn bậc hai của 4 là: ", sqrt(4) )
```

Câu lệnh import trong chương trình trên chỉ dùng được hàm sqrt, các hàm khác của module không dùng được.

Xem xét thêm chương trình sau:

```python
from math import sqrt, pi
print("Căn bậc hai của 4 là: ", sqrt(4) )
print('Pi = ', pi)
```

Hoặc 

```python
from math import *
print("Căn bậc hai của 4 là: ", sqrt(4) )
print('Pi = ', pi)
```

Cả 2 chương trình trên đều có Output: `Căn bậc hai của 4 là:  2.0  
Pi =  3.141592653589793`

## Lưu file Module ở đâu?

File module phải được lưu trữ trong phạm vi thư mục cho phép của Python thì chương trình mới có thể gọi và import vào để sử dụng.

Khi import, Python sẽ tìm kiếm file module ở nhiều nơi. Trình thông dịch sẽ tìm kiếm một mô-đun tích hợp sẵn trước. Sau đó \(nếu không tìm thấy mô-đun tích hợp sẵn\), Python sẽ tìm trong các thư mục được xác định trong sys.path. 

Việc tìm kiếm ưu tiên theo thứ tự sau:

* Thư mục hiện tại \(thư mục lưu file chương trình chính\). 
* PYTHONPATH \(một biến liệt kê danh sách các thư mục\). 
* Thư mục cài đặt Python. 

Ta có thể xem Python parth mặc định bằng lệnh path trong module sys

```python
import sys
print(sys.path)
```

## Trong file module có gì?

Để xem trong file module có những đối tượng nào đã được định nghĩa ta dùng câu lệnh dir\(tên module\). Ví dụ:

```python
import math
print(dir(math))
```

Output: `['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']`



Muốn biết đối tượng \(hàm\) được định nghĩa trong module có chức năng gì ta dùng phương thức gọi docstring. 

Ví dụ, ta thử xem hàm có tên factorial trong module math có chức năng gì:

```python
import math
print(math.factorial.__doc__)
```

 Output: `Find x!.  
Raise a ValueError if x is negative or non-integral.`

