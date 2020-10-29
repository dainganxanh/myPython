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

```python
import os
os.chdir('C:\\Python')     # ví dụ chuyển sang thư mục Python trong ổ C
```

### Xem nội dung thư mục 

Để xem trong thư mục có chứa gì ta dùng hàm listdir\(\). Hàm trả về một list là tên các file và thư mục con có trong thư mục đang làm việc.

```python
import os

noidung = os.listdir()
print(noidung)        # list liệt kê tên file và subfolder
```

### Tạo thư mục mới

```python
import os
os.mkdir('thumucmoi')
```

### Xóa thư mục hoặc file

Sử dụng phương thức remove\(\) để xóa file và rmdir\(\) để xóa folder \(chỉ xóa được folder trống\).

```python
import os
os.remove('filename.txt')     # xóa file có tên: filename.txt
os.rmdir('foldername')        # xóa folder có tên: foldername
print(os.listdir())
```

Để xóa một thư mục không trống, ta có thể sử dụng phương thức rmtree\(\) thuộc module shutil

```python
import shutil

shutil.rmtree('fodername')
print(os.listdir())
```





