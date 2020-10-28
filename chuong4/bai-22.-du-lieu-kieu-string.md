# Bài 22. Dữ liệu kiểu string

Một xâu \(string - chuỗi\) là một dãy các ký tự. Một ký tự chỉ đơn giản là một biểu tượng \(một lần nhấn phím\). Ví dụ, ngôn ngữ tiếng Anh có 26 ký tự. 

Máy tính không xử lý các ký tự, chúng xử lý các số \(nhị phân\). Mặc dù ta có thể nhìn thấy các ký tự trên màn hình của mình, nhưng bên trong nó vẫn được lưu trữ và thao tác dưới dạng kết hợp của 0 và 1. 

Quá trình chuyển đổi ký tự thành số này được gọi là mã hóa và quá trình ngược lại là giải mã. ASCII và Unicode là các bảng mã được sử dụng phổ biến. 

Trong Python, string là một chuỗi các ký tự **Unicode**. Unicode là bảng mã có thể biểu diễn mọi ký tự trong tất cả các ngôn ngữ hiện nay trên thế giới. 

## Khởi tạo string

Các ký tự được đặt trong cặp nháy đơn, kép, ba nháy đơn được gọi là một xâu \(string\). Một xâu có thể có 1 hoặc nhiều ký tự. Xâu không chứa ký tự gọi là xâu rỗng.

Ví dụ:

```python
s = 'Hello'
print(s)           # Hello

s = "Hello"
print(s)           # Hello

s = '''Hello'''
print(s)           # Hello

s = """Hello, welcome to
           the world of Python"""
print(s)           
# với ba nháy đơn hoặc ba nháy kép cho phép string viết trên nhiều dòng
```

## Truy cập ký tự trong string

Ta có thể truy cập từng ký tự của chuỗi thông qua chỉ số. Chỉ số của các ký tự trong chuỗi được bắt đầu từ 0 và theo chiều ngược lại được bắt đầu từ -1.

Ví dụ:

```python
str = 'Python3'
print('str = ', str)               # str =  Python3

print('str[0] = ', str[0])         # str[0] =  P

print('str[-1] = ', str[-1])       # str[-1] =  3

print('str[1:5] = ', str[1:5])     # str[1:5] =  ytho

print('str[3:-2] = ', str[3:-2])   # str[3:-2] =  ho
```

Chỉ số chỉ có thể là số nguyên trong phạm vi từ 0 đến chiều dài xâu - 1. 

## Thêm, sửa, xóa ký tự trong string

String không cho phép sửa đổi ký tự sau khi gán. Ta chỉ có thể ghép xâu với toán tử +, \* hoặc gán lại giá trị mới cho xâu. Ta cũng có thể xóa biến xâu bằng từ khoá del.

Ví dụ:

```python
a = "Học "
b = "Python "
c = a + b
print(c)        # Học Python 
print(c*3)      # Học Python Học Python Học Python 

c = c + "rất vui"
print(c)        # Học Python rất vui

del a
print(a) # báo lỗi: NameError: name 'a' is not defined
```

Lưu ý: \(1\) Khi viết 2 string gần nhau sẽ cho kết quả như sử dụng phép cộng 2 string. \(2\) Ta có thể nối các string trên các dòng khác nhau bằng dấu ngoặc.

Ví dụ:

```python
a = "học " "python"

b = ("học "
     "Python "
     "thật vui")

print(a)          # học python
print(b)          # học python thật vui
```

##   Kiểm tra xâu con chứa trong xâu

Ta có thể kiểm tra xem một xâu con có tồn tại trong một xâu hay không bằng cách sử dụng từ khóa in. 

```python
a = "học python"
print('a' in a)        # False
print('py' in a)       # True 
print('x' not in a)    # True
```

## Lặp theo ký tự của xâu

```python
a = 'Hello World'
count = 0
for x in a:
    if(x == 'l'):
        count += 1
print(f'Tìm thấy {count} chữ l trong xâu "{a}"')
# output: Tìm thấy 3 chữ l trong xâu "Hello World"
```

## Hàm dựng sẵn cho string

Có nhiều hàm để làm việc với xâu. Các hàm thường dùng khi làm việc với xâu là hàm len\(\) và emurate\(\).

```python
a = 'done'

lst_a = list(enumerate(a))
dic_a = dict(enumerate(a))
len_a = len(a)

print(lst_a)    # [(0, 'd'), (1, 'o'), (2, 'n'), (3, 'e')]
print(dic_a)    # {0: 'd', 1: 'o', 2: 'n', 3: 'e'}
print(len_a)    # 4
```

## Định dạng xâu

Yêu cầu 1: Viết chương trình in ra màn hình dòng sau: `He said, "What's there?"`

Nếu ta dùng cặp nháy đơn hay nháy kép đều sẽ gặp lỗi vì bản thân câu trên đã có chứa cả nháy đơn và nháy kép. 

Cách xử lý là dùng cặp ba nháy đơn hoặc dùng ký tự "\" để bỏ qua dấu khóa string. Ví dụ:

```python
a = '''He said, "What's there?"'''
b = 'He said, "What\'s there?"'
c = "He said, \"What's there?\""

print(a)    # He said, "What's there?"
print(b)    # He said, "What's there?"
```

Yêu cầu 2: Viết chương trình in ra màn hình dòng sau: `C:\My Documents\noname`

Trong Python, khi gặp dấu \ thì Python sẽ coi ký tự tiếp theo là một ký tự xâu bình thường và không coi nó là toán tử hay keyword nữa \(trừ những toán tử, keyword đi kèm dấu \\).  

Vì vậy trong trường hợp ta muốn Python coi dấu \ là một ký tự thông thường thì ta phải thêm từ khóa r vào trường nháy mở xâu.

Ví dụ, chạy thử chương trình sau để thấy sự khác nhau giữa 2 câu lệnh

```python
print('C:\My Documents\noname')
print(r'C:\My Documents\noname')
```

### Một số thao tác khác với dấu \

| Lệnh | Ý nghĩa |
| :--- | :--- |
| \a | ASCII Bell \(âm báo\) |
| \b | ASCII Backspace \(xóa lùi\) |
| \f | ASCII Formfeed \(trang mới\) |
| \n | ASCII Linefeed \(dòng mới\) |
| \r | ASCII Carriage Return  |
| \t | ASCII Horizontal Tab \(tab ngang\) |
| \v | ASCII Vertical Tab \(tab dọc\) |
| \ooo | Character with octal value ooo \(Ký tự có giá trị bát phân là ooo\) |
| \xHH | Character with hexadecimal value HH \(Ký tự có giá trị thập lục phân là HH\) |

### Định dạng với f-string

Xét ví dụ dưới đây:

```python
a = 12
b = 12.3456789
c = ['hoa', 'lá', 'cành']

print("Biểu diễn nhị phân của {a} là {a:b}".format(a))
print(f"Biểu diễn dạng số mũ của {a} là {a:e}")
print(f'Số {a} có thể viết thành: {a:.4f}')
print(f'Số {b} có thể viết thành {b:.2f}')
print(f'|{c[0]:<10}|{c[2]:^20}|{c[1]:>10}|')
```

### Định dạng theo phương thức format\(\)

```python
a = 36
b = 12.3456789
c = ['hoa', 'lá', 'cành']

print("Biểu diễn nhị phân của {0} là {0:b}".format(a))
print("Biểu diễn dạng số mũ của {0} là {0:e}".format(a))
print('Số {0} có thể viết thành: {0:.4f}'.format(a))
print('Số {0} có thể viết thành {0:.2f}'.format(b))
print('|{0:<10}|{2:^20}|{1:>10}|'.format(c[0],c[1],c[2]))
```

## Phương thức thường dùng

Python có rất nhiều phương thức làm việc với string. Một số phương pháp thường được sử dụng là  lower\(\), upper\(\), join\(\), split\(\), find\(\), replace\(\)... 

Ví dụ:

```python
a = 'Học Python'
a = a.upper()
print(a)            # HỌC PYTHON
a = a.lower()
print(a)            # học python
a = a.split()
print(a)            # ['học', 'python']
a = ' '.join(a)
print(a)            # học python
t = a.find('c')
print(t)            # 2
a = a.replace('học','learn')    
print(a)            # learn python
```

Có thể tham khảo [các phương thức khác làm việc với string tại đây](https://www.programiz.com/python-programming/methods/string).

