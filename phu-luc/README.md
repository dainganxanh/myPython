---
description: 'Ghi chép trong quá trình vừa biên soạn,vừa thực hành'
---

# Phụ lục

### Bung nén tham số tuple, dict

```python
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

a = (12, 40, 99)
b = {'x': 31, 'z': 'MA', 'y': 88}

myfunc(*a)
myfunc(**b)
```

### Lấy chỉ số list \(list index\)

```python
lst = [1,2,3]
print(lst.index(3))
# out: 2
```

### Đảo ngược list, string

```python
s = 'abcd'
ms = list(s)
ss = s[::-1]
mss = ms[::-1]

print(ss)        # dcba
print(ms)        # ['a', 'b', 'c', 'd']
print(mss)       # ['d', 'c', 'b', 'a']
```

### Cắt xâu string, list \(slide\)

```python
s = '123456789'
ss = list(s)

print(s[:2])
print(s[-2:])
print(s[1:-2])

print(ss[:2])
print(ss[-2:])
print(ss[1:-2])
```

### Remove phần tử trùng lặp trong list

Đơn giản chỉ bằng cách ép kiểu set và trả lại list

```python
a = [1,1,2,3,4,5,4,5,4]
a = list(set(a))
print(a)

# Output: [1, 2, 3, 4, 5]
```

### Ép kiểu phần tử list

Chuyển các phần tử của list từ str sang int và ngược lại. [Xem thêm bài map\(\) ](ham-map.md)

```python
a = ['1','2','3','4','5']
b = ['1','2','3','4','5']
a = list(map(int,a))           # cách 1
b = [int(i) for i in b]        # Cách 2
print(a, b) 

# Output: [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
```

###  Phân biệt list, tuple, set, dict

Khác biệt giữa List, Dict, Tuple, Set trong Python

| Tên | Đặc trưng | Sửa phần tử | Sắp xếp | Đặt trong dấu | Khởi tạo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| List | Chứa bất kì kiểu dữ liệu nào | x | x | \[\] | list\(\) |
| Tuple | Giá trị không thể thay đổi |  | x | \(\) | tuple\(\) |
| Set | Giá trị là duy nhất | x |  | {} | set\(\) |
| Dict | Key: Value | x |  | {} | dict\(\) |

