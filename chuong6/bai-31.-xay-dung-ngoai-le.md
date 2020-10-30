---
description: Ngoại lệ do người dùng tự định nghĩa
---

# Bài 31. Xây dựng ngoại lệ

Ví dụ, chương trình sau yêu cầu nhập một số thỏa điều kiện, lặp đến khi nào người dùng nhập đúng mới thôi.

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

