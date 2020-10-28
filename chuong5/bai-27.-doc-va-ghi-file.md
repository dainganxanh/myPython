# Bài 27. Đọc và ghi file

Việc đọc và ghi tệp chúng ta đã được tìm hiểu ở bài 8 chương I. Trong bài này sẽ trình bày chi tiết hơn một số vấn đề liên quan đến việc đọc và ghi tệp trong Python.

Để thao tác với tệp \(đọc hoặc ghi dữ liệu\) trong Python có nhiều cách khác nhau. Trong đó sử dụng câu lện with là đơn giản và hiệu quả, ngắn gọn và an toàn. Cú pháp như sau:

```python
with open("tenfile.txt", 'mode') as tenbien:   
    # Thực hiện các thao tác với file
```

Với câu lệnh trên file được mở để thao tác đồng thời sẽ tự động đóng file sau khi thao tác.

Cách khác, ta có thể dùng cấu khối lệnh sau:

```python
try:
   f = open("test.txt",'mode')
   # Thực hiện các thao tác với file
finally:
   f.close()
```

Các chế độ mở file \(mode\) thường dùng như sau:

<table>
  <thead>
    <tr>
      <th style="text-align:left"><b>Mode</b>
      </th>
      <th style="text-align:left"><b>T&#xE1;c &#x111;&#x1ED9;ng</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">r</td>
      <td style="text-align:left">M&#x1EDF; ch&#x1EC9; &#x111;&#x1EC3; &#x111;&#x1ECD;c. (m&#x1EB7;c &#x111;&#x1ECB;nh)</td>
    </tr>
    <tr>
      <td style="text-align:left">w</td>
      <td style="text-align:left">
        <p>M&#x1EDF; &#x111;&#x1EC3; ghi, n&#x1EBF;u &#x111;&#xE3; c&#xF3; n&#x1ED9;i
          dung th&#xEC; s&#x1EBD; ghi &#x111;&#xE8;.</p>
        <p>N&#x1EBF;u file ch&#x1B0;a t&#x1ED3;n t&#x1EA1;i th&#xEC; t&#x1EA1;o file
          m&#x1EDB;i.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">x</td>
      <td style="text-align:left">T&#x1EA1;o file &#x111;&#x1ED9;c quy&#x1EC1;n m&#x1EDB;i (exclusive creation)
        v&#xE0; ghi n&#x1ED9;i dung, n&#x1EBF;u file &#x111;&#xE3; t&#x1ED3;n t&#x1EA1;i
        th&#xEC; ch&#x1B0;&#x1A1;ng tr&#xEC;nh s&#x1EBD; b&#xE1;o l&#x1ED7;i.</td>
    </tr>
    <tr>
      <td style="text-align:left">a</td>
      <td style="text-align:left">
        <p>M&#x1EDF; file ch&#x1EBF; &#x111;&#x1ED9; ghi ti&#x1EBF;p.</p>
        <p>N&#x1EBF;u file &#x111;&#xE3; t&#x1ED3;n t&#x1EA1;i r&#x1ED3;i th&#xEC;
          n&#xF3; s&#x1EBD; ghi ti&#x1EBF;p n&#x1ED9;i dung v&#xE0;o cu&#x1ED1;i
          file, n&#x1EBF;u file kh&#xF4;ng t&#x1ED3;n t&#x1EA1;i th&#xEC; t&#x1EA1;o
          m&#x1ED9;t file m&#x1EDB;i.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">t</td>
      <td style="text-align:left">M&#x1EDF; file &#x1EDF; ch&#x1EBF; &#x111;&#x1ED9; v&#x103;n b&#x1EA3;n
        (m&#x1EB7;c &#x111;&#x1ECB;nh)</td>
    </tr>
    <tr>
      <td style="text-align:left">b</td>
      <td style="text-align:left">M&#x1EDF; file &#x1EDF; ch&#x1EBF; &#x111;&#x1ED9; nh&#x1ECB; ph&#xE2;n</td>
    </tr>
  </tbody>
</table>

## 1. Đọc file <a id="1-doc-file"></a>

Ví dụ, Ta có file ‘vao.txt’ được lưu cùng thư mục với file Python.

Mở file để đọc ta dùng phương thức **`with open(‘tenfile’, ‘mode’) as tenbien`**. Ta có thể gán mode hoặc bỏ qua vì Python mặc định mở file là để đọc.

### **Đọc toàn bộ file**

```python
with open("vao.txt") as f:   
    print(f.read())
```

### **Đọc từng dòng \(1 dòng\)**

```python
with open("vao.txt") as f:    
    print(f.readline())
```

### **Đọc từng dòng \(2 dòng\)**

```python
with open("vao.txt") as f:    
    print(f.readline())    
    print(f.readline())
```

### **Đọc từng dòng đến hết file**

```python
with open("vao.txt") as f:    
    for i in f:        
        print(i, end='')
```

**Lưu ý:** Tất cả dữ liệu đọc từ file text đều có kiểu string. Vì vậy nếu là các chữ số, khi đọc vào phải ép kiểu thành number mới có thể thực hiện các phép toán số học.

Chúng ta có thể thay đổi vị trí con trỏ tệp hiện tại bằng cách sử dụng phương thức seek \(\). Tương tự, phương thức tell \(\) trả về vị trí hiện tại của con trỏ tệp \(theo số byte\).

Ví dụ:

```python
with open('input.txt') as f:    
    print(f.read())    
    print(f.tell())        
    f.seek(0)    
    doc = f.read(5)    
    print(doc)    
    print(f.tell())    
    f.seek(13)    
    print(f.read())
```

**Giải thích:** 

Câu lệnh 1 để mở file đọc   
Câu lệnh 2 đọc toàn bộ file và in ra màn hình   
Câu lệnh 3: in ra màn hình thông báo vị trí con trỏ hiện thời \(là vị trí cuối file\)   
Câu lệnh 4: chuyển con trỏ về vị trí 0 \(đầu file\)   
Câu lệnh 5: đọc 5 ký tự \(5 bytes\) và gán vào biến doc   
Câu lệnh 6: in biến doc ra màn hình   
Câu lệnh 7: in ra màn hình thông báo vị trí con trỏ hiện thời   
Câu lệnh 8: Chuyển con trỏ đến vị trí 13   
Câu lệnh 9: đọc đến cuối file và in ra màn hình

Output:

`Learn Python together   
21   
Learn   
5   
together`

## 2. Mở file để ghi <a id="2-mo-file-de-ghi"></a>

Mở file để ghi ta dùng phương thức **with open\(‘tenfile’, ‘mode’\) as tenbien**. Mode thường dùng là **w** \(ghi đè\) hoặc **a** \(ghi tiếp\).

Cả mode **a** và **w** đều sẽ tạo file mới để ghi nếu file mở để ghi chưa tồn tại.

Ví dụ:

```python
with open("ra.txt",'w') as f:    
    f.write("Ghi dong chu nay vao file ra.txt")
```

Lưu ý: Để ghi dữ liệu vào file text ta chuyển về kiểu xâu trước khi ghi \(nếu dữ liệu là số\).

Chương trình sau sẽ báo lỗi:

```python
a = "Ghi dong chu nay vao file ra.txt"
b = 994
with open("ra.txt",'w') as f:    
    f.write(a + '\n')    
    f.write(b)
```

Ta sửa lỗi như sau:

```python
a = "Ghi dong chu nay vao file ra.txt"
b = 994
with open("ra.txt",'w') as f:    
    f.write(a + '\n')    
    f.write(str(b))
```

[  
](https://python.dainganxanh.com/chuong1/bai-7.-kieu-du-lieu-trong-python)

