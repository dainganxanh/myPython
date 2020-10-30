---
description: Lỗi và ngoại lệ trong Python
---

# Bài 29. Ngoại lệ

Một chương trình python sẽ dừng lại ngay khi nó gặp lỗi nếu chưa được khắc phục. Những lỗi này có thể được phân thành 2 loại:

* Lỗi cú pháp 
* Lỗi logic \(Ngoại lệ\)

## Lỗi cú pháp

Lỗi do không tuân theo cấu trúc \(cú pháp\) của ngôn ngữ được gọi là lỗi cú pháp \(syntax error\) hoặc lỗi phân tích cú pháp \(parsing error\).

Ví dụ:

```python
print(hello world!)
```

Khi chạy chương trình sẽ báo lỗi:

```python
Traceback (most recent call last):
  File "C:\...\main.py", line 1
    print(hello world!)
                    ^
SyntaxError: invalid syntax
```

Chương trình phát sinh lỗi ở dòng 1, vị trí trong hàm print \(xâu "hello world!" chưa có dấu nháy mở-đóng xâu\)

## Lỗi logic \(ngoại lệ - exceptions\)

Các lỗi xảy ra khi chạy chương trình \(sau khi vượt qua kiểm tra cú pháp\) được gọi là ngoại lệ \(exceptions\) hoặc lỗi lôgic \(logical errors\).

Ví dụ, lỗi sẽ phát sinh khi ta mở một file không tồn tại \(FileNotFoundError\),khi ta thực hiện phép chia cho 0 \(ZeroDivisionError\), khi ta import một module không tồn tại \(ImportError\),...

Bất cứ khi nào các loại lỗi logic xảy ra, Python sẽ tạo một đối tượng ngoại lệ. Nếu không được xử lý đúng cách, nó sẽ in thông báo lỗi cùng với một số chi tiết về lý do tại sao lỗi đó xảy ra.

Xem xét ví dụ sau:

```python
a = 1 / 0
```

Chạy chương trình sẽ nhận được thông báo sau:

```python
Traceback (most recent call last):
  File "C:\...\main.py", line 1, in <module>
    a = 1 / 0
ZeroDivisionError: division by zero
```
```python
open("imaginary.txt")
Traceback (most recent call last):
 File "<string>", line 301, in runcode
 File "<interactive input>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
```
# Ngoại lệ dựng sẵn

