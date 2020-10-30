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



