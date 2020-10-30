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

Bất cứ khi nào các loại lỗi logic \(runtime error\) xảy ra, Python sẽ phát sinh một đối tượng ngoại lệ. Nếu không được xử lý đúng cách, chương trình sẽ in thông báo lỗi cùng với một số chi tiết về lý do tại sao lỗi đó xảy ra.

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

| **Ngoại lệ** | **Lý do gây ra** |
| :--- | :--- |
| AssertionError | Xảy ra khi câu lệnh assert thất bại. |
| AttributeError | Xảy ra khi gán thuộc tính hoặc tham chiếu thất bại. |
| EOFError | Xảy ra khi hàm input \(\) chạm vào điều kiện end-of-file. |
| FloatingPointError | Xảy ra khi một số thực dấy phẩy động thực thi không thành công |
| GeneratorExit | Xảy ra khi phương thức close\(\) của hàm generator được gọi. |
| ImportError | Xảy ra khi không tìm thấy module được import. |
| IndexError | Xảy ra khi một chỉ số trong chuỗi \(sequence\) nằm ngoài phạm vi. |
| KeyError | Xảy ra khi không tìm thấy khóa ánh xạ \(từ điển\) trong tập hợp các khóa hiện có. |
| KeyboardInterrupt | Xảy ra khi người dùng nhấn phím ngắt \(thông thường là Ctrl-C hoặc Delete\). |
| MemoryError | Xảy ra khi một operation hết bộ nhớ nhưng tình huống vẫn có thể được sửa chữa \(bằng cách xóa một số đối tượng\). |
| NameError | Xảy ra khi không tìm thấy tên cục bộ hoặc toàn cầu của biến. |
| NotImplementedError | Xảy ra bằng các phương thức trừu tượng khi chúng yêu cầu các lớp dẫn xuất ghi đè phương thức. |
| OSError | Xảy ra khi một hàm trả về lỗi liên quan đến hệ thống |
| OverflowError | Xảy ra khi kết quả của phép toán số học quá lớn không thể biểu diễn. |
| ReferenceError | Xảy ra khi một proxy tham chiếu yếu sử dụng để truy cập một thuộc tính của tham chiếu sau khi thu thập rác. |
| RuntimeError | Xảy ra khi phát hiện thấy lỗi không thuộc bất kỳ danh mục nào khác. |
| StopIteration | Xảy ra bằng phương thức next\(\) của một vòng lặp để báo hiệu rằng không có giá trị nào được trả về bởi iterator. |
| SyntaxError | Xảy ra khi gặp lỗi cú pháp. |
| IndentationError | Xảy ra khi có lỗi thụt lề không chính xác. |
| TabError | Xảy ra khi thụt lề sử dụng các tab và dấu cách không nhất quán. |
| SystemError | Xảy ra khi trình thông dịch tìm thấy các lỗi nội bộ nhưng tình hình không quá nghiêm trọng. |
| SystemExit | Xảy ra bởi hàm sys.exit\(\). |
| TypeError | Xảy ra khi một hàm hoặc phép thực thi \(operation\) áp dụng kiểu không chính xác cho một đối tượng. |
| UnboundLocalError | Xảy ra khi tham chiếu tạo thành một biến cục bộ trong một hàm hoặc phương thức, nhưng không có giá trị nào bị ràng buộc với biến đó. |
| UnicodeError | Xảy ra khi có lỗi liên quan đến Unicode |
| UnicodeEncodeError | Xảy ra khi lỗi liên quan đến Unicode diễn ra trong quá trình mã hóa. |
| UnicodeDecodeError | Xảy ra khi lỗi liên quan đến Unicode diễn ra trong quá trình giải mã. |
| UnicodeTranslateError | Xảy ra khi lỗi liên quan đến Unicode trong quá trình dịch. |
| ValueError | Xảy ra khi một phép toán hoặc hàm nhận được một đối số có kiểu đúng nhưng giá trị không phù hợp |
| ZeroDivisionError | Xảy ra khi đối số thứ hai của phép chia hoặc phép toán modulo bằng 0. |

Chúng ta có thể xử lý các ngoại lệ bằng cách sử dụng câu lệnh try, except và finally \(sẽ tìm hiểu trong bài học tiếp theo\).

