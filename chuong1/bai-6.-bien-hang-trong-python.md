# Bài 6. Biến, Hằng

## 1. Biến và câu lệnh gán

Biến là một đối tượng trong chương trình. Mỗi biến sẽ có một vị trí riêng trong bộ nhớ để lưu trữ dữ liệu \(giá trị\) được gán. Biến trong Python được đặt theo nguyên tắc định danh \(xem lại mục 2.2\).

Câu lệnh gán giá trị cho biến là: &lt;tên biến&gt; = &lt;giá trị gán cho biến&gt;

Biến trong Python không cần khai báo trước, không gần khai báo kiểu dữ liệu. Khi đặt tên và gán giá trị Python tự động nhận dạng và tùy biến theo kiểu dữ liệu được gán.

Ví dụ 1:

```python
number = 10
number = 1.1
print(number)
input()
```

Ở ví dụ trên, biến được đặt tên là number, được gán giá trị là 10 sau đó lại được gán giá trị là 1.1. Như vậy sau sau 2 câu lệnh trên giá trị của biến number lưu sẽ là 1.1. Kết quả khi chạy chương trình là: 1.1.

Ví dụ 2.

```python
website = "dainganxanh.com"
print(website)
# assigning a new variable to website
website = "hocdeday.com"
print(website)
input()
```

Ở ví dụ này, biến có tên website được gán giá trị là dainganxanh.com sau đó được in ra bởi câu lệnh print\(website\). Sau đó lại được gán giá trị mới và thực hiện lệnh in lần 2.

Kết quả sẽ là:

> dainganxanh.com  
> hocdeday.com

Python cho phép gán nhiều giá trị cho nhiều biến trong cùng một câu lệnh gán. Ví dụ:

```python
a, b, c = 5, 3.2, "Hello"
print (a)
print (b)
print (c)
```

Các toán tử gán khác được trình bày trong mục 9.5

## 2. Hằng

Hằng là một loại biến đặc biệt, giá trị của hằng là không đổi trong suốt chương trình sau lần gán giá trị đầu tiên. Tên hằng được viết hoàn toàn bằng chữ hoa và dấu gạch dưới \(nếu cần\).

Ví dụ:

```python
PI = 3.14 # đây là hằng
bankinh = 20 # đây là biến
```

Trong thực tế, việc đặt tên Hằng bằng các ký tự in hoa là để phân biệt với biến chứ nó không có tác dụng ngăn cản việc gán giá trị mới cho Hằng.

Đối với các chương trình lớn, Hằng số thường được khai báo riêng trong một mô-đun. Mô-đun là một tệp riêng chứa các biến, hàm, v.v. được nhập \(import\) vào tệp chính.

Ví dụ:

Tạo một file mới với tên “hang.py” trong cùng thư mục với file “thuchanh.py”.

-         Nội dung file hang.py:

```python
PI = 3.14
GRAVITY = 9.8
```

-         Nội dung file thuchanh.py:

```python
import hang
print(hang.PI)
print(hang.GRAVITY)
input()
```

Chạy file thuchanh.py sẽ cho kết quả là:

> 3.14  
> 9.8

