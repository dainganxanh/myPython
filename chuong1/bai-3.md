# Bài 3. Câu lệnh, khối lệnh và chú thích

## 1. Câu lệnh

Những hướng dẫn mà trình thông dịch Python có thể thực hiện được gọi là các câu lệnh. Ví dụ, a = 1 là một lệnh gán. Lệnh if, lệnh for, lệnh while,... là những loại lệnh khác mà chúng ta sẽ được tìm hiểu chi tiết trong các bài sau.

Thông thường mỗi dòng là một câu lệnh. Ví dụ, chương trình sau gồm 2 câu lệnh:

```python
a = 5
print(a)
```

Lưu ý: Khác với C++ và Pascal, Python không cần dấu ; để kết thúc câu lệnh.

Nhiều câu lệnh có thể được viết trên cùng một dòng nhưng phải được phân cách nhau bởi dấu chấm phẩy ; . Ví dụ, chương trình dưới đây gồm 3 câu lệnh:

```python
a = 1; b = 2; c = 3
```

Một câu lệnh cũng có thể viết trên nhiều dòng với điều kiện: sử dụng dấu nối dòng \ hoặc các dòng được đặt trong dấu ngoặc \(\), \[\], {}.

Ví dụ:

```python
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
```

Hoặc

```python
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
```

Hoặc

```python
colors = ['red',
        'blue', 'green'
        ]
```

### 1.2      Khối lệnh

Nếu Pascal, C++ hay Java dùng cặp ngoặc nhọn để bao một khối lệnh thì Python lại dùng cách thụt đầu dòng để đánh dấu khối lệnh.

Một khối lệnh \(thường là khối lệnh của hàm, vòng lặp,...\) bắt đầu với thụt lề và kết thúc với dòng đầu tiên không thụt lề. Thụt lề bao nhiêu là tùy ý nhưng chúng phải nhất quán trong suốt khối lệnh đó \(các lệnh trong cùng một khối thì phải có độ thụt lề bằng nhau\).

Ví dụ:

```python
for i in range(1,11):
    print(i)
    if i == 5:
        break
input()
```

Cũng chương trình trên nhưng nếu chúng ta viết lại như sau sẽ bị báo lỗi và chương trình không được thực thi:

```python
for i in range(1,11): 
  print(i); 
    if i == 5:
        break
input()
```

Lý do báo lỗi là do các lệnh thuộc vòng for không được thụt lề giống nhau \(print và if là cùng cấp \(cùng nằm trong lệnh for:\) nên phải được thụt lề như nhau\)

### 1.3      Chú thích trong Python

Chú thích trên một dòng được bắt đầu bằng dấu thăng \#

Chú thích nhiều dòng được đặt trong cặp ba dấu nháy đơn """

Ví dụ: Cả 2 chương trình dưới đây đều in ra chữ “Hello”

```python
#This is a comment
#print out Hello
print('Hello')
input() 
```

\# input\(\) để dừng màn hình như readline;\(Pascal\) hay getch\(\);\(C++\)

Và

```python
"""This is also a perfect example of
multi-line comments"""
print('Hello')
input()
```

### 1.4      Docstring – Chú thích đối tượng

Docstring là viết tắt của Documentation string - chuỗi tài liệu, dùng để chú thích tóm tắt chức năng cho những đối tượng \(mô đun, hàm, method,…\).

Ba dấu nháy kép được sử dụng để viết docstring như ví dụ dưới đây:

```python
def nhandoi(num):
    """Hàm nhân đôi giá trị nhập vào"""
    return 2*num
```

Viết như trên, sau này ta có thể tra cứu \(in ra\) docstring của hàm để biết chức năng của hàm đã viết. Cách in như sau:

```python
print(nhandoi.__doc__)
```

Kết quả sẽ là: “`Hàm nhân đôi giá trị nhập vào`”  


