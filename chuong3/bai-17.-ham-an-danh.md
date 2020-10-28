# Bài 17. Hàm ẩn danh

Hàm ẩn danh không dùng từ khóa def và tên hàm. Cú pháp hàm ẩn danh như sau:

```python
<tên biến> = lambda <tham số>: <biểu thức / giá trị trả về>
```

Ví dụ

```python
tong3 = lambda a, b, c : a + b + c
x = 5
y = 7
z = 3
print(tong3(x,y,z)
```

Output: `15`

Các hàm lambda có thể có nhiều tham số nhưng chỉ có một biểu thức. Các hàm Lambda có thể được sử dụng ở bất cứ nơi nào trong chương trình.

Ví dụ 2

```python
double = lambda x: x * 2
print(double(5))
```

Chương trình trên tương đương với:

```python
def double(x):
   return x * 2
print(double(5))
```

Hàm Lambda được sử dụng cùng với các hàm có sẵn như filter \(\), map \(\), v.v. 

Khi sử dụng cùng với các hàm có sẵn \(build-in\), lambda thường được dùng như một tham số của hàm build-in. 

Ví dụ

```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)
```

Output: `[4, 6, 8, 12]`

```python
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)
```

Output: `[2, 10, 8, 12, 16, 22, 6, 24]`

Trong ví dụ trên, lambda là tham số thứ nhất của hàm filter\(\), map\(\).



