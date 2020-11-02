# Bài 1. Cài đặt môi trường

## **Python là gì ?**

```python
print('Python là gì?') 
```

Python là một ngôn ngữ lập trình bậc cao do Guido van Rossum tạo ra và lần đầu ra mắt vào năm 1991. Python vừa hướng thủ tục \(procedural-oriented\), vừa hướng đối tượng \(object-oriented\) đồng thời có thể nhúng vào ứng dụng như một giao tiếp kịch bản \(scripting interface\).

Thế mạnh của Python là rất gần gũi với ngôn ngữ tự nhiên \(tiếng Anh\), cấu trúc rõ ràng, dễ đọc, dễ học. Python hiện nay là ngôn ngữ lập trình phổ biến rộng rãi ở châu Âu, châu Mỹ và được coi như **ngôn ngữ lập trình trường học**.

Python được dùng để phát triển các ứng dụng web, game, khoa học dữ liệu \(tính toán, phân tích, khai thác dữ liệu\), máy học và trí tuệ nhân tạo, …

## 1.    Cài Python

Tải về từ [https://www.python.org/downloads/](https://www.python.org/downloads/) và tiến hành cài đặt \(chọn phiên bản 3.8 trở lên\).

Sau khi hoàn tất cài đặt có thể kiểm tra:

-        Nhấn phím Windows gõ cmd à Enter

-        Gõ: python --version à Enter

Lúc này sẽ hiển thị phiên bản Python đã cài đặt trên máy tính.

## 2.    Trình soạn thảo

Để lập trình theo một ngôn ngữ nào đó ta đều cần có chương trình cho phép gõ các câu lệnh và ra lệnh thực thi các câu lệnh đó. Trong các trường học, để lập trình với Pascal ta thường sử dụng FreePascal, với C ta thường dùng CodeBlock, … Với Python, ta có nhiều lựa chọn. 

Dưới đây là một số gợi ý cho người mới học Python:

### 1\) Python Online Compiler

Search với từ khóa "Python Online Compiler" sẽ trả về kết quả với nhiều website khác nhau. Ví dụ [https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/) là một ứng dụng được cung cấp bởi Progamiz.

### **2\)**    **Notepad++, Sublime Text, ...**

Tải Notepad++ về tại đây: [https://notepad-plus-plus.org/downloads/](https://notepad-plus-plus.org/downloads/)

Tải Sublime Text về tại đây: [https://www.sublimetext.com/3](https://www.sublimetext.com/3) 

Đặc điểm: Đơn giản, dễ sử dụng.

Nhược điểm: Phải cài đặt plugin, thiết lập thêm mới có thể run python code.

### **3\)**    **Thonny**

Tải về tại đây: [https://thonny.org/](https://thonny.org/)

Thonny có giao diện đơn giản, cấu hình nhẹ \(trên cùng một máy khởi động nhanh hơn nhiều so với Pycham hay Spyder\). Hỗ trợ debug trực quan giúp ta dễ theo dõi và hình dung quá trình thực thi chương trình. Sử dụng thư viện / module chuẩn của Python phát hành \(không bổ sung hay import sẵn module\).

### **4\)**    **PyCharm Educational Edition**

Tải về tại đây: [https://www.jetbrains.com/pycharm-edu/](https://www.jetbrains.com/pycharm-edu/)

PyCharm là môi trường phát triển tích hợp đa nền tảng \(IDE\) được phát triển bởi Jet Brains và được thiết kế đặc biệt cho Python. Tuy nhiên PyCharm khởi động khá nặng nề và yêu cầu làm việc với project. Như vậy, tùy nhu cầu sử dụng và kỹ năng lập trình mà chúng ta lựa chọn trình soạn thảo cho phù hợp. Đối với người mới bắt đầu học Python thì nên dùng Thonny để thực hành.

## 3. Chương trình đầu tiên

Viết chương tình đầu tiên với ngôn ngữ lập trình Python trên máy tính của bạn như sau:

Mở Notepad++ và gõ:

```python
print("Hello world !")
input()
```

Lưu với tên: Hello.py

Double click để chạy file Hello.py sẽ cho kết quả “`Hello world !`”

