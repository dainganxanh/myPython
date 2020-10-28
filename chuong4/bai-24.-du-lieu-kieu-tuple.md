# Bài 24. Dữ liệu kiểu tuple

Tuple trong Python tương tự như list. Sự khác biệt giữa hai kiểu dữ liệu này là tuple không thể thay đổi các phần tử khi nó đã được gán còn list thì có thể thay đổi.

## Khởi tạo tuple

```python
mb = ()    # tuple rỗng
print(mb)

mb = (1, 2, 3)    # tuple các số nguyên
print(mb)

mb = (1, "Hello", 3.4)    # tuple hỗn hợp
print(mb)

mb = ("mouse", [8, 4, 6], (1, 2, 3))     # tuple lồng nhau
print(mb)
```

Ta có thể gán phần tử cho tuple mà không cần dùng dấu ngoặc đơn.

```python
mb = 1, 2, 3
a,b,c = mb

print(a)    # 1
print(b)    # 2
print(c)    # 3

print(mb)     # (1, 2, 3)
```

**Lưu ý** khi khởi tạo tuple chỉ có một phần tử phải đặt dấu phẩy sau phần tử nếu không Python sẽ nhận diện đó là một str.

```python
mb = ("hello")
print(type(mb))  # <class 'str'> 

mb = ("hello",)
print(type(mb))  # <class 'tuple'>

# Parentheses is optional
mb = "hello",
print(type(mb))  # <class 'tuple'>

```

## Truy cập phần tử tuple

Ta sử dụng chỉ số trong cặp ngoặc \[\] để truy cập phần tử tuple. Chỉ số các phần tử trong tuple bắt đầu từ 0 và chiều ngược lại bắt đầu từ -1.

Việc truy cập phần tử tuple cũng tương tự như truy cập phần tử list. Ví dụ:

```python
mt = ('P', 'y', 't', 'h', 'o', 'n', '3')

print(mt[1])   # y
print(mt[5])   # n
print(mt[-6])  # y

# tuple lồng nhau
mm = ("mouse", [8, 4, 6], (1, 2, 3))
print(mm[0][3])       # 's'
print(mm[1][1])       # 4    
```

## Cắt tuple

```python
mt = ('P', 'y', 't', 'h', 'o', 'n', '3')

print(mt[1:4])    # ('y', 't', 'h')
print(mt[:-6])    # ('P',)
print(mt[6:])     # ('3',)
print(mt[:])      # ('P', 'y', 't', 'h', 'o', 'n', '3')

print(mt[::-1])    # ('3', 'n', 'o', 'h', 't', 'y', 'P')
```

## Thêm, sửa, xóa phần tử tuple

### Thêm

Khác với list, tuple không cho phép thay đổi giá trị phần tử. 

Để thêm phần tử vào tuple ta có thể dùng toán tử cộng + để nối tuple; toán tử \* để nhân tuple. Ví dụ:

```python
a = (1, 2, 3)
aa = a + (4, 5, 6)
print(aa)             # (1, 2, 3, 4, 5, 6)

aaa = a*2
print(aaa)            # (1, 2, 3, 1, 2, 3)
```

### Sửa

Như định nghĩa ban đầu, tuple không cho phép sửa đổi phần tử khi đã gán. 

Tuy nhiên, nếu phần tử của tuple ở dạng list thì ta vẫn có thể can thiệp vào phần tử của list.

Một cách khác để sửa phần tử tuple là gán cho biến tuple một tập giá trị mới.

Ví dụ:

```python
mt = (4, 2, 3, [6, 5])

mt[3][0] = 9
print(mt)                # (4, 2, 3, [9, 5])

mt = (4, 6, 8, [6, 5])
print(mt)                # (4, 6, 8, [6, 5])
```

### Xóa

Tuple không xóa được từng phần tử mà chỉ có thể xóa hoàn toàn biến tuple

```python
mt = ('P', 'y', 't', 'h', 'o', 'n', '3')
del mt
print(mt)     # báo lỗi: NameError: name 'mt' is not defined
```

## Phương thức \(tuple method\)

Khác với list, tuple chỉ có 2 phương thức hoạt động đó là count\(\) và index\(\). Ví dụ:

```python
mt= ('a', 'p', 'p', 'l', 'e',)

print(mt.count('p'))  # Output: 2
print(mt.index('l'))  # Output: 3
```

## Thao tác khác

### Kiểm tra phần tử chứa trong tuple

```python
mt = ('P', 'y', 't', 'h', 'o', 'n', '3')

print('t' in mt)        # True
print('z' in mt)        # False
print('g' not in mt)    # True
```

### Lặp theo phần tử tuple

```python
mt = ('xanh', 'đỏ', 'tím', 'vàng')

for x in mt:
    print("Tôi thích màu", x)
```

Output: `Tôi thích màu xanh  
Tôi thích màu đỏ  
Tôi thích màu tím  
Tôi thích màu vàng`

## Khi nào dùng tuple thay vì list?

* Thường ta nên dùng list cho dữ liệu đồng nhất \(cùng kiểu\) và dùng tuple cho dữ liệu không đồng nhất.
* Truy xuất phần tử tuple nhanh hơn list nên hiệu suất tốt hơn \(chỉ đáng kể với dữ liệu lớn\).
* Tuple có thể dùng làm key cho dict. list thì không.
* Nếu dữ liệu cần được đảm bảo không thay đổi thì tuple là lựa chọn \(phần tử của tuple không thể thay đổi\).

