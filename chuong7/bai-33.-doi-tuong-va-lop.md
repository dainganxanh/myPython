---
description: Python Objects and Classes
---

# Bài 33. Đối tượng và Lớp

Đối tượng \(Object\) chỉ đơn giản là một tập hợp các dữ liệu \(các biến\) và các phương thức \(các hàm\) hoạt động trên các dữ liệu đó. Và, lớp \(class\) là một kế hoạch chi tiết cho đối tượng.

Ta có thể hình dung class như một bản phác thảo \(nguyên mẫu\) của một ngôi nhà. Nó chứa tất cả các chi tiết về sàn nhà, cửa ra vào, cửa sổ,... Dựa trên những mô tả này, chúng ta sẽ xây \(hoặc in 3D\) các ngôi nhà và nhà ở đây chính là đối tượng.

### Khai báo một Class <a id="define"></a>

Cú pháp khai báo \(định nghĩa\) một Class như sau

```python
class TenClass:
    '''Đây là docstring để ghi chú cho class'''
    # các câu lệnh trong thân class 
```

Một class tạo ra một không gian tên cục bộ \(local namespace\) mới nơi tất cả các thuộc tính của nó được định nghĩa. Các thuộc tính có thể là dữ liệu hoặc hàm.

Ngoài ra còn có các thuộc tính đặc biệt được bắt đầu bằng dấu gạch dưới kép \_\_**. Ví dụ:** `__doc__`  cung cấp cho chúng ta docstring của class.

Ngay sau khi chúng ta định nghĩa một Class, một đối tượng lớp mới có cùng tên cũng được tạo. Đối tượng lớp này cho phép chúng ta truy cập các thuộc tính khác nhau cũng như khởi tạo các đối tượng mới của lớp đó.

```python
class Hocsinh:
    "Đây là một class có tên là Hocsinh"
    tuoi = 10

    def chao(self):
        print('Xin chào!')


# Output: 10
print(Hocsinh.tuoi)

# Output: <function Hocsinh.chao>
print(Hocsinh.chao)

# Output: 'Đây là một class có tên là Hocsinh'
print(Hocsinh.__doc__)
```

### Tạo đối tượng \(Object\) <a id="create"></a>

Đối tượng trong class có thể được sử dụng để truy cập các thuộc tính khác nhau và tạo các instance mới của lớp đó. Thủ tục để tạo một đối tượng tương tự như cách chúng ta gọi hàm.

```python
hs = Hocsinh()
```

Thao tác trên sẽ tạo một đối tượng mới có tên là hs. Chúng ta có thể truy cập các thuộc tính của đối tượng bằng tiền tố tên đối tượng. 

Các thuộc tính có thể là dữ liệu hoặc phương thức. Các phương thức của một đối tượng là các hàm tương ứng của lớp đó.

Xem ví dụ sau:

```python
class Hocsinh:
    tuoi = 10

    def chao(self):
        print('Xin chào!')


# Tạo một đối tượng mới theo class Hocsinh
hs = Hocsinh()

# Output: <function Hocsinh.chao at ... >
print(Hocsinh.chao)

# Output: <bound method Hocsinh.chao of <__main__.Hocsinh object at ...>>
print(hs.chao)

# Gọi phương thức chao()
# Output: Xin chào!
hs.chao()
```

**Output**

```python
<function Hocsinh.chao at 0x00000133B8A57EE0>
<bound method Hocsinh.chao of <__main__.Hocsinh object at 0x00000133B8A45FD0>>
Xin chào!
```

Tham số self của hàm trong class là tham số mặc định ngầm gán bởi chính đối tượng mỗi khi đối tượng được gọi. Việc gọi phương thức chao\(\) thông qua đối tượng  `hs.chao()` tương đương với gọi phương thức chao\(\) từ Class `Hocsinh.chao(hs)`.

### Constructors  <a id="constructor"></a>

Hàm trong Class được bắt đầu với dấu gạch dưới kép `__` là các hàm đặc biệt, mang các ý nghĩa đặc biệt. Một trong đó là hàm `__init__()`. Hàm này được gọi bất cứ khi nào khởi tạo một đối tượng, một biến mới trong class và được gọi là **constructor** trong lập trình hướng đối tượng.

```python
class SoPhuc:

    def __init__(self, r=0, i=0):
        self.thuc = r
        self.ao = i

    def hienthi(self):
        print(f'{self.thuc}+{self.ao}j')


# Tạo đối tượng 
num1 = SoPhuc(2, 3)

# Gọi phương thức hienthi()
# Output: 2+3j
num1.hienthi()

# Tạo đối tượng SoPhuc khác
# thêm thuộc tính 'attr'
num2 = SoPhuc(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.thuc, num2.ao, num2.attr))

# thuộc tính 'attr' được tạo cho đối tượng num2 nhưng không tồn tại cho num1
# AttributeError: 'SoPhuc' object has no attribute 'attr'
# print(num1.attr)
```

**Output**

```text
2+3j
(5, 0, 10)
```

### Xóa bỏ thuộc tính và đối tượng

Any attribute of an object can be deleted anytime, using the `del` statement. Try the following on the Python shell to see the output.

```python
class SoPhuc:
    def __init__(self, r=0, i=0):
        self.thuc = r
        self.ao = i

    def hienthi(self):
        print(f'{self.thuc}+{self.ao}j')


# Tạo đối tượng 
num1 = SoPhuc(2, 3)

# Gọi phương thức hienthi()
# Output: 2+3j
num1.hienthi()

# Tạo đối tượng SoPhuc khác
# thêm thuộc tính 'attr'
num2 = SoPhuc(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.thuc, num2.ao, num2.attr))

# thuộc tính 'attr' được tạo cho đối tượng num2 nhưng không tồn tại cho num1
# AttributeError: 'SoPhuc' object has no attribute 'attr'
# print(num1.attr)

# xóa phần ảo của đối tượng num1
del num1.ao 
# Lệnh sau sẽ gây lỗi vì không tồn tại thuộc tính 'ao'
# 'SoPhuc' object has no attribute 'ao'
print(num1.hienthi())


del SoPhuc.hienthi
# AttributeError: 'SoPhuc' object has no attribute 'hienthi'
print(num1.hienthi())

```

Ta có thể xóa bằng chính tên đối tượng với câu lệnh `del`.

```python
c1 = SoPhuc(1,3)
del c1
# NameError: name 'c1' is not defined
print(c1)
```



