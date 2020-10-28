# Bài 14. Hàm

Hàm là một nhóm các lệnh có liên quan đến nhau được dùng để thực hiện một tác vụ, nhiệm vụ cụ thể nào đó. Hàm giúp chia chương trình Python thành những phần nhỏ hơn - giúp chương trình có tổ chức và dễ quản lý hơn.

Hàm còn có một tác dụng vô cùng quan trọng nữa là tránh việc phải lặp lại code để thực thi những tác vụ tương tự nhau, giúp code gọn hơn và có thể tái sử dụng.

## 1. Cú pháp

```python
def <tenham>(<biến/danh sách biến>):
   """docstring (ghi chú về chức năng của hàm/
   hàm không nhất thiết phải có docstring)"""
   <lệnh/ khối lệnh thực hiện nhiệm vụ>
```

Ví dụ:

```python
def chao(name):
    """
    Đây là hàm in một câu chào hỏi 
    với biến nhập vào là tên người được chào
    """
    print("Hello, " + name + ". Good morning!")
chao('Dosing')         # gọi hàm

# Output: Hello, Dosing. Good morning!
```

Lệnh gọi docstring \(đọc chú thích của hàm\)

`print(<tên hàm>.__doc__)`

Ví dụ:

```python
print(chao.__doc__)

# Output: Đây là hàm in một câu chào hỏi với biến nhập vào là tên người được chào
```

## 2. Câu lệnh return

Lệnh return thường được dùng để thoát hàm và trở về nơi mà tại đó hàm được gọi.

```python
def trituyetdoi(num):
    """Hàm trả về giá trị tuyệt đối"""
    if num >= 0:
        return num
    else:
        return -num
print(trituyetdoi(2))
print(trituyetdoi(-4))

# Output:
#    2
#    4
```



## 3. Phạm vi biến

Biến trong hàm được gọi là biến cục bộ \(local\) có phạm vi trong hàm chứa biến. Biến ngoài hàm có phạm vi trong toàn chương trình được gọi là biến toàn cục \(global\).

Ví dụ

```python
def my_func():
        x = 10
        print("Giá trị của biến x trong hàm:", x)
x = 20
my_func()
print("Giá trị của biến x bên ngoài hàm:", x)

# Output:
#        Giá trị của biến x trong hàm: 10 
#        Giá trị của biến x ngoài hàm: 20
```

_Ở ví dụ trên, nếu không khai báo biến x = 20 ở dòng 4 thì chương trình sẽ báo lỗi._

Để khai báo một biến trong hàm là biến toàn cục \(global\) thì ta dùng từ khóa global. Ví dụ như sau:

```python
def my_func():
        x = 10
        global y
        y = 15
        print("Giá trị của biến x,y trong hàm:", x, y)
x = 20
my_func()
print("Giá trị của biến x,y bên ngoài hàm:", x, y)
```

## 4. Phân loại hàm

Hàm trong Python được phân làm 2 loại gồm 

* [Hàm có sẵn \(build-in\) ](https://www.programiz.com/python-programming/built-in-function)
* [Hàm do người dùng xây dựng \(user-defined\).](https://www.programiz.com/python-programming/user-defined-function)





