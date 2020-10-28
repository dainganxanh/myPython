# Bài 2. Từ khóa và định danh

## 1. Từ khóa \(keywords\)

Từ khóa \(keyword\) là những tên dành riêng của Python, chúng được định nghĩa sẵn để sử dụng. Chúng ta không thể dùng keyword để đặt tên biến, tên hàm hoặc bất kỳ đối tượng nào trong chương trình.

Ví dụ một số keyword: True, False, await, else, import, pass, break, except, in, and, or, ….

Tất cả các keyword trong Python đều được viết thường, trừ 03 key word: True, False, None.

Thực tế thì không cần nhớ keyword vì khi gõ trình soạn thảo sẽ có gợi ý các keyword \(ta tránh đặt tên đối tượng trùng với các keyword được gợi ý\) và nếu đặt trùng tên keyword thì khi chạy chương trình sẽ báo lỗi.

## 2. Định danh \(Identifiers\)

Định danh là việc đặt tên cho các đối tượng trong chương trình như tên hàm, tên biến, lớp,… Tên các đối tượng được đặt bằng các ký tự thường \(a-z\), ký tự in hoa \(A-Z\), chữ số \(0-9\) và dấu gạch dưới \_ . Ví dụ: bien1, lop, var\_1, …

Tên đối tượng không bắt đầu bằng chữ số. không dùng các ký tự đặc biệt như !, @, \#, … và được phân biệt chữ hoa, chữ thường.

Lưu ý: Nên đặt tên đối tượng có tính gợi nhớ. Ví dụ, với một biến đếm, thay vì đặt d = 10 thì ta nên đặt là dem = 10 .

Ví dụ chương trình đơn giản:

```python
A = 2
a = 3
tong = a+A
tich = a*A
print(a)
print(A)
print("Tổng a và A là",tong)
print("Tích a và A là",tich)
input()
```



