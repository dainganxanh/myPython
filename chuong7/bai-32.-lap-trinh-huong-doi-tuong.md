---
description: Python Object Oriented Programming
---

# Bài 32. Lập trình hướng đối tượng

Lập trình hướng đối tượng \(Object-oriented programming, viết tắt: OOP\) là một kỹ thuật hỗ trợ, cho phép lập trình viên trực tiếp làm việc với các đối tượng mà họ định nghĩa lên. Hiệu quả của kĩ thuật này giúp tăng năng suất, đơn giản hoá độ phức tạp khi bảo trì cũng như mở rộng phần mềm. 

Khái niệm về OOP trong Python tập trung vào việc tạo code sử dụng lại. Khái niệm này còn được gọi là DRY \(Don't Repeat Yourself\). OOP trong Python tuân theo một số nguyên lý cơ bản là tính đóng gói, tính kế thừa và tính đa hình.

* Tính kế thừa \(Inheritance\): cho phép một lớp \(class\) có thể kế thừa các thuộc tính và phương thức từ các lớp khác đã được định nghĩa.
* Tính đóng gói \(Encapsulation\): là quy tắc yêu cầu trạng thái bên trong của một đối tượng được bảo vệ và tránh truy cập được từ code bên ngoài \(tức là code bên ngoài không thể trực tiếp nhìn thấy và thay đổi trạng thái của đối tượng đó\).
* Tính đa hình \(Polymorphism\): là khái niệm mà hai hoặc nhiều lớp có những phương thức giống nhau nhưng có thể thực thi theo những cách thức khác nhau.

## Lớp \(Class\) và Đối tượng \(Object\)

Class và Object là hai khái niệm cơ bản trong lập trình hướng đối tượng.

Đối tượng \(Object\) là những thực thể tồn tại có hành vi.

Ví dụ đối tượng là một xe ô tô có tên hãng, màu sắc, loại nguyên liệu, hành vi đi, dừng, đỗ, nổ máy...

Lớp \(Class\) là một kiểu dữ liệu đặc biệt do người dùng định nghĩa, tập hợp nhiều thuộc tính đặc trưng cho mọi đối tượng được tạo ra từ lớp đó.

Thuộc tính là các giá trị của lớp. Sau này khi các đối tượng được tạo ra từ lớp, thì thuộc tính của lớp lúc này sẽ trở thành các đặc điểm của đối tượng đó.

### Lớp \(Class\)

Ta có thể hình dung class giống như là một bản mẫu \(template\), một khuôn mẫu. Ở đó ta khai báo các thuộc tính \(attribute\) và phương thức \(method\) nhằm miêu tả để từ đó ta tạo ra được những object \(đối tượng\).

Cú pháp để tạo một lớp

```python
class <tên_lớp>:
    code thuộc tính và phương thức
```

Ví dụ:

```python
class ChimVet:
    pass
```

### Đối tượng \(Object\)

Một đối tượng \(còn gọi là instance\) là một khởi tạo của một lớp. 

Khi lớp được định nghĩa, chỉ có mô tả cho đối tượng được định nghĩa. Do đó, không có bộ nhớ hoặc bộ nhớ nào được cấp phát. Khi khai báo đối tượng bằng việc gán cho một class thì lúc này bộ nhớ được cấp phát cho đối tượng. 

Ví dụ

```python
v1 = Chimvet()
```



