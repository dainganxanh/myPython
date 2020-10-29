# Bài 28. Quản lý file và folder

Trong bài này, ta sẽ tìm hiểu về quản lý tệp và thư mục bằng Python, cách tạo một thư mục, đổi tên, liệt kê tất cả các thư mục và làm việc với thư mục.

Python có module os cung cấp cho chúng ta nhiều phương pháp hữu ích để làm việc với folder và file.

## Làm việc với module os

### Xác định thư mục hiện tại

```python
import os

a = os.getcwd()
b = os.getcwdb()
print(a)            # in ra đường dẫn đến thư mục hiện tại (kiểu str)
print(type(a))    # <class 'str'>

print(b)            # in ra đường dẫn đến thư mục hiện tại (kiểu bytes)
print(type(b))    # <class 'bytes'>
```

### Mở thư mục khác \(chuyển thư mục làm việc\)



