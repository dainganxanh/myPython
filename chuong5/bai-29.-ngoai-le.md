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



