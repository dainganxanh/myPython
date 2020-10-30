# Bài 30. Xử lý ngoại lệ

Trong bài này chúng ta tìm tìm hiểu cách xử lý các ngoại lệ trong chương trình Python bằng câu lệnh try, exception và finally.

## Bắt ngoại lệ

Các câu lệnh xử lý chính có thể phát sinh ngoại lệ được đặt bên trong lệnh try. Các lệnh xử lý ngoại lệ được đặt bên trong câu lệnh except.

Để lấy tên ngoại lệ ta dùng phương thức exc\_info\(\) trong module sys. Ví dụ như sau

```python
import sys

ma = ['a', 0, 2, 5]

for i in ma:
    try:
        print("Giá trị phần tử là", i)
        r = 1/int(i)
        print("Nghịch đảo của ", i, "là", r)
    except:
        print("Phát sinh ngoại lệ:", sys.exc_info()[0])
        print("Xét phẩn tử tiếp theo:")
```

Output:  
`Giá trị phần tử là a  
Phát sinh ngoại lệ: <class 'ValueError'>  
Xét phẩn tử tiếp theo:  
Giá trị phần tử là 0  
Phát sinh ngoại lệ: <class 'ZeroDivisionError'>  
Xét phẩn tử tiếp theo:  
Giá trị phần tử là 2  
Nghịch đảo của  2 là 0.5  
Giá trị phần tử là 5  
Nghịch đảo của  5 là 0.2`

Ở ví dụ trên, phần tử đầu tiên là 'a' không thể thực hiện phép tính r = 1/'a' nên phát sinh ngoại lệ "`ValueError`" , phần tử thứ 2 là 0 phát sinh ngoại lệ "`ZeroDivisionError`" khi thực hiện phép tính 1/0.

Vì tất cả các ngoại lệ tích hợp sẵn đều kế thừa từ class Exception trong module sys nên ta có thể viết chương trình trên theo cách sau:

```python
import sys

ma = ['a', 0, 2, 5]

for i in ma:
    try:
        print("Giá trị phần tử là", i)
        r = 1/int(i)
        print("Nghịch đảo của ", i, "là", r)
    except Exception as ex:
        print("Phát sinh ngoại lệ:", ex.__class__ )
        print("Xét phẩn tử tiếp theo:")
```

## Bắt ngoại lệ cụ thể

Ta có thể dự đoán ngoại lệ phát sinh để bắt và xử lý theo từng trường hợp. 

Chỉ định ngoại lệ cụ thể cho khối lệnh except với cú pháp như sau:

```python
try:
 # khối lệnh try
except exceptionName:
 # khối lệnh except
except exceptionName2:
 # khối lệnh except 2
```

Ví dụ 

```python
ma = ['a', 0, 2, 5]

for i in ma:
    try:
        print("Giá trị phần tử là", i)
        r = 1/int(i)
        print("Nghịch đảo của ", i, "là", r)
        print()
    except ValueError:
        print("Lỗi giá trị phần tử không phù hợp.")
        print("Xét phẩn tử tiếp theo:")
        print()
    except ZeroDivisionError:
        print("Lỗi mẫu số bằng 0.")
        print("Xét phẩn tử tiếp theo:")
        print()
```

Ta cũng có thể bắt nhiều ngoại lệ trong một lệnh except. Ví dụ:

```python
ma = ['a', 0, 2, 5]

for i in ma:
    try:
        print("Giá trị phần tử là", i)
        r = 1/int(i)
        print("Nghịch đảo của ", i, "là", r)
        print()
    except (ValueError, ZeroDivisionError):
        print("Lỗi giá trị phần tử không phù hợp.")
        print("Xét phẩn tử tiếp theo:")
        print()
```

## Câu lệnh try else

Trong một số trường hợp, ta có thể muốn chạy một khối lệnh nhất định nào đó khi khối lệnh trong try không có bất kỳ lỗi nào. Đối với những trường hợp này, ta có thể sử dụng từ khóa else với câu lệnh try.

```python
try:
    num = int(input("Nhập một số chẵn: "))
    assert num % 2 == 0
except:
    print("Không phải số chẵn!")
else:
    r = 1/num
    print(f'Số nghị đảo của {num} là {r}')
```

Chương trình trên chỉ xử lý trường hợp được coi là ngoại lệ khi số nhập vào không là số chẵn. Các ngoại lệ khác sẽ không được xử lý. Ví dụ nhập vào số 0 thì chương trình sẽ báo lỗi ZeroDivisionError.

## Câu lệnh try finally

Câu lệnh try... finally được thực thi bất kể điều gì, và thường được sử dụng để giải phóng các tài nguyên bên ngoài như kết thúc phiên làm việc kết nối với trung tâm dữ liệu từ xa thông qua mạng hoặc làm việc với tệp hoặc Giao diện người dùng...

Ví dụ: đóng file sau khi mở và thao tác với file

```python
try:
   f = open("test.txt")
   # các thao tác xử lý file
finally:
   f.close()
```

