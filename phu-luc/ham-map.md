# Hàm map\(\)

Hàm map\(\) trong Python sẽ duyệt và thực hiện thao tác với từng phần tử của mảng \(list, set, tuple\) và trả về kết quả sau khi thao tác. 

map\(\) có thể dùng thay vòng lặp for, while trong nhiều trường hợp. Xét các ví dụ sau

Ví dụ 1

Dùng for:

```python
def binhphuong(n):
    return n*n

a = (2, 5, 3, 100)
kq = []
for i in a:
    kq.append(binhphuong(i))

print(kq)
```

Dùng map\(\)

```python
def binhphuong(n):
    return n*n

a = (2, 5, 3, 100)
kq = map(binhphuong, a)

print(list(kq))
```

Ví dụ 2. Dùng lambda trong map\(\)

```python
a = (1, 2, 3, 4)
kq = map(lambda x: x*x, a)

kq = tuple(kq)
print(kq)
```

Ví dụ 3. Dùng map tính toán phần tử mảng

```python
num1 = [4, 5, 6]
num2 = [5, 6, 7]

cong = map(lambda n1, n2: n1+n2, num1, num2)
nhan = map(lambda n1, n2: n1*n2, num1, num2)

print(list(cong))
print(list(nhan))
```

Ví dụ 4. Chuyển đổi kiểu dữ liệu phần tử mảng và tính toán

```python
ch1 = ['4', '5', '6']
num2 = [5, 6, 7]

num1 = list(map(int, ch1))     # thao tác ép kiểu phần tử list

cong = map(lambda n1, n2: n1+n2, num1, num2)
print(list(cong))
```

