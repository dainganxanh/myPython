---
description: Lỗi và ngoại lệ trong Python
---

# Bài 29. Ngoại lệ

Một chương trình python sẽ dừng lại ngay khi nó gặp lỗi nếu chưa được khắc phục. Những lỗi này có thể được phân thành 2 loại:

* Lỗi cú pháp 
* Lỗi logic \(Ngoại lệ\)

### Lỗi cú pháp

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

### Lỗi logic \(ngoại lệ - exceptions\)

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

Ví dụ về lỗi mở file không tồn tại:

```python
open("imaginary.txt")
Traceback (most recent call last):
 File "<string>", line 301, in runcode
 File "<interactive input>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
```

## Ngoại lệ tích hợp sẵn \(built-in exceptions\)

Hoạt động không hợp lệ sẽ sinh ngoại lệ. Có rất nhiều ngoại lệ tích hợp sẵn trong Python được gọi ra khi các lỗi tương ứng xảy ra. Ta có thể xem tất cả các ngoại lệ được tích hợp sẵn bằng cách sử dụng hàm local\(\) được tích hợp sẵn như sau:

```python
print(dir(locals()['__builtins__']))
```

Một số ngoại lệ tích hợp sẵn phổ biến trong Python cùng với lỗi gây ra chúng được liệt kê dưới đây:

| Exception | Cause of Error |
| :--- | :--- |
| `AssertionError` | Raised when an `assert` statement fails. |
| `AttributeError` | Raised when attribute assignment or reference fails. |
| `EOFError` | Raised when the `input()` function hits end-of-file condition. |
| `FloatingPointError` | Raised when a floating point operation fails. |
| `GeneratorExit` | Raise when a generator's `close()` method is called. |
| `ImportError` | Raised when the imported module is not found. |
| `IndexError` | Raised when the index of a sequence is out of range. |
| `KeyError` | Raised when a key is not found in a dictionary. |
| `KeyboardInterrupt` | Raised when the user hits the interrupt key \(`Ctrl+C` or `Delete`\). |
| `MemoryError` | Raised when an operation runs out of memory. |
| `NameError` | Raised when a variable is not found in local or global scope. |
| `NotImplementedError` | Raised by abstract methods. |
| `OSError` | Raised when system operation causes system related error. |
| `OverflowError` | Raised when the result of an arithmetic operation is too large to be represented. |
| `ReferenceError` | Raised when a weak reference proxy is used to access a garbage collected referent. |
| `RuntimeError` | Raised when an error does not fall under any other category. |
| `StopIteration` | Raised by `next()` function to indicate that there is no further item to be returned by iterator. |
| `SyntaxError` | Raised by parser when syntax error is encountered. |
| `IndentationError` | Raised when there is incorrect indentation. |
| `TabError` | Raised when indentation consists of inconsistent tabs and spaces. |
| `SystemError` | Raised when interpreter detects internal error. |
| `SystemExit` | Raised by `sys.exit()` function. |
| `TypeError` | Raised when a function or operation is applied to an object of incorrect type. |
| `UnboundLocalError` | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| `UnicodeError` | Raised when a Unicode-related encoding or decoding error occurs. |
| `UnicodeEncodeError` | Raised when a Unicode-related error occurs during encoding. |
| `UnicodeDecodeError` | Raised when a Unicode-related error occurs during decoding. |
| `UnicodeTranslateError` | Raised when a Unicode-related error occurs during translating. |
| `ValueError` | Raised when a function gets an argument of correct type but improper value. |
| `ZeroDivisionError` | Raised when the second operand of division or modulo operation is zero. |

Chúng ta có thể xử lý các ngoại lệ bằng cách sử dụng câu lệnh try, except và finally \(sẽ tìm hiểu trong bài học tiếp theo\).

