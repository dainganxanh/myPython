---
description: Ngoại lệ do người dùng tự định nghĩa
---

# Bài 31. Xây dựng ngoại lệ

Trong lập trình Python, các ngoại lệ phát sinh khi lỗi logic. Ta cũng có thể sinh các ngoại lệ theo cách thủ công bằng cách sử dụng từ khóa raise.

Hãy xét một số ví dụ dưới đây và thực hành xây dựng ngoại lệ

## Ví dụ 1

Chương trình yêu cầu nhập một số thỏa điều kiện, lặp đến khi nào người dùng nhập đúng mới thôi.

```python
while True:
    try:
        x = int(input('Nhập một số nguyên trong khoảng 1-10: '))
        if x<1 or x>10:
            raise Exception
        print(f'Bạn vừa nhập một số hợp lệ: x = {x}')
        break
    except:
        print('Số vừa nhập ngoài khoảng cho phép. Nhập lại nhé!')
```

```python
while True:
    try:
        a = int(input("Nhập số nguyên dương: "))
        if a <= 0:
                raise ValueError("Đó không phải là số nguyên dương!")
        else: break
    except ValueError as ex:
            print(ex)

print(f'Thực hiện các thao tác với {a}')
```

## Ví dụ 2

Trò chơi đoán số

```python
class Loi(Exception):
    """Lớp cơ sở cho những ngoại lệ khác"""
    pass

class SoNhoQua(Loi):
    """Phát sinh khi số nhập vào nhỏ quá"""
    pass

class SoLonQua(Loi):
    """Phát sinh khi số nhập vào lớn quá"""
    pass

# Sinh ngẫu nhiên một số nguyên
import random as rd
number = rd.randint(1,100)

# nhập số đoán
landoan = 0
while True:
    try:
        n = int(input("Nhập vào số nguyên: "))
        landoan +=1
        if n < number:
            raise SoNhoQua
        elif n > number:
            raise SoLonQua
        break
    except SoNhoQua:
        print("Số này chưa đủ lớn - nhập lại nhé!")
        print()
    except SoLonQua:
        print("Số này lớn quá, thử lại xem!")
        print()

print(f"Xin chúc mừng! Bạn đã đoán chính xác trong {landoan} lần đoán.")
```

