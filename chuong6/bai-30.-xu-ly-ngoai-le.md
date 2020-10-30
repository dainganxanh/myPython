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



