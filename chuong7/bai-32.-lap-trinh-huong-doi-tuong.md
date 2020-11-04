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

Ví dụ đối tượng là một con chim vẹt có tên, màu sắc, trọng lượng, hành vi \(tập nói, ăn, bay, nhảy...\)...

Lớp \(Class\) là một kiểu dữ liệu đặc biệt do người dùng định nghĩa, tập hợp nhiều thuộc tính đặc trưng cho mọi đối tượng được tạo ra từ lớp đó.

Thuộc tính là các giá trị của lớp. Sau này khi các đối tượng được tạo ra từ lớp, thì thuộc tính của lớp lúc này sẽ trở thành các đặc điểm của đối tượng đó.

## Lớp \(Class\)

Ta có thể hình dung class giống như là một bản mẫu \(template\), một khuôn mẫu. Ở đó ta khai báo các thuộc tính \(attribute\) và phương thức \(method\) nhằm miêu tả để từ đó ta tạo ra được những object \(đối tượng\).

Cú pháp để tạo một lớp

```python
class <tên_lớp>:
    code thuộc tính và phương thức
```

Ví dụ:

```python
class ConVet:
    pass
```

Thông thường \(và theo chuẩn format code Python PEP8\) thì tên lớp được viết hoa chữ đầu từ \(CapWord\).

## Đối tượng \(Object\)

Một đối tượng \(còn gọi là instance\) là một khởi tạo của một lớp. 

Khi lớp được định nghĩa, chỉ có mô tả cho đối tượng được định nghĩa. Do đó, không có bộ nhớ hoặc bộ nhớ nào được cấp phát. Khi khai báo đối tượng bằng việc gán cho một class thì lúc này bộ nhớ được cấp phát cho đối tượng. 

Ví dụ

```python
v1 = ConVet()
```

Ví dụ 1. Tạo class và object trong Python

```python
class ConVet:
    loai = "chim"

    def __init__(self, name, age):
        self.name = name
        self.age = age

em = ConVet("Vẹt Em", 10)
anh = ConVet("Vẹt Anh", 15)

# truy xuất thuộc tính class
print(f'Vẹt thuộc loài {anh.__class__.loai}')

# truy xuất thuộc tính đối tượng
print(f"{anh.name} {anh.age} năm tuổi")
print(f"{em.name} {em.age} năm tuổi")
```

Output:

```python
Vẹt thuộc loài chim
Vẹt Anh 15 năm tuổi
Vẹt Em 10 năm tuổi
```

Trong chương trình trên, ta đã tạo một class với tên ConVet và khai báo các thuộc tính \(đặc tính của một đối tượng\).

Các thuộc tính được định nghĩa bên trong phương thức \_\_init\_\_ của lớp. Đây là phương thức khởi tạo \(constructor\) được gọi đầu tiên ngay sau khi đối tượng được tạo.

Trong chương trình, ta tạo 2 đối tượng \(thể hiện\) của lớp ConVet gồm ble và woo.

Ta gọi thuộc tính class bằng cú pháp: \_\_class\_\_.&lt;tên thuộc tính lớp&gt; \(vd. \_\_class\_\_.loai\); gọi thuộc tính đối tượng với cú pháp: &lt;tên đối tượng&gt;.&lt;tên thuộc tính&gt; \(vd: blu.name, blu.age\).

## Phương thức \(Methods\)

Các phương thức là các hàm được định nghĩa bên trong phần thân của một lớp. Chúng được sử dụng để xác định các hành vi của một đối tượng.

Ví dụ

```python
class ConVet:
	# thuộc tính
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # phương thức
    def sing(self, song):
        return f"{self.name} hát bài {song}"

    def dance(self):
        return f"{self.name} đang nhảy múa"

# khởi tạo đối tượng
em = ConVet("Vẹt em", 10)

# gọi phương thức
print(em.sing("AAAAAAAAAAAA"))
print(em.dance())
```

Output:

```python
Vẹt em hát bài AAAAAAAAAAAA
Vẹt em đang nhảy múa
```

## Kế thừa \(Inheritance\)

Kế thừa là một cách tạo một lớp mới để sử dụng các chi tiết của một lớp hiện có mà không cần sửa đổi nó. Lớp mới được hình thành là một lớp dẫn xuất \(hoặc lớp con\). Tương tự, lớp hiện có là một lớp cơ sở \(hoặc lớp cha\).

Ví dụ

```python
# parent class (lớp cha)
class Chim:
    
    def __init__(self):
        print("Chim được khởi tạo")

    def boi(self):
        print("Bơi nhanh ")

    def bay(self):
        print("Chim hầu hết là biết bay")    

    def noio(self):
    	print('Hoang dã')

# child class (lớp con)
class CanhCut(Chim):

    def __init__(self):
        # gọi hàm super()
        super().__init__()
        print("Cánh cụt được khởi tạo")

    def chay(self):
        print("Chạy nhanh ")

    def bay(self):
        print("Chim cánh cụt thì không biết bay nhé")        

chimA = Chim()
chimA.bay()
chimA.boi()
print()

chimZ = CanhCut()
chimZ.boi()
chimZ.chay()
chimZ.noio()
chimZ.bay()
```

Output:

```python
Chim được khởi tạo
Chim hầu hết là biết bay
Bơi nhanh 

Chim được khởi tạo
Cánh cụt được khởi tạo
Bơi nhanh 
Chạy nhanh 
Hoang dã
Chim cánh cụt thì không biết bay nhé
```

Trong ví dụ trên ta dễ thấy lớp CanhCut thừa kế từ lớp Chim. Qua đó, đối tượng chimZ có thể gọi phương tức boi\(\) và noio\(\) trong khi lớp CanhCut không hề khai báo.

## Đóng gói \(Encapsulation\)



