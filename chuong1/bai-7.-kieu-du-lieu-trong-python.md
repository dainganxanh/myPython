# Bài 7. Kiểu dữ liệu

**Bài này giới thiệu sơ lược các kiểu dữ liệu trong Python.** Trong chương IV chúng ta sẽ tìm hiểu sâu về từng kiểu dữ liệu và các thao tác xử lý đối với từng kiểu dữ liệu.

## 1. Kiểu số \(numbers\)

Python sử dụng các kiểu số thường dùng trong lập trình như số nguyên \(int\), số thực \(float\) và số phức \(complex\). Ta có thể dùng hàm type\(\) để kiểm tra xem dữ liệu thuộc kiểu nào và dùng lện  isinstance\(\) để xem số liệu có thuộc về một kiểu nào đó hay không.

Ví dụ:

```python
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
```

Output:

> 5 is of type &lt;class 'int'&gt;
>
> 2.0 is of type &lt;class 'float'&gt;
>
> \(1+2j\) is complex number? True

### -         **Số nguyên \(int\)**

Số nguyên trong Python không gới hạn độ dài mà chỉ phụ thuộc vào bộ nhớ của máy.

### -         **Số thực \(float\)**

Số thực khác số nguyên bởi phần thập phân. Số chữ thập phân tối đa trong Python là 15 chữ số.

### -         **Số phức \(complex\)**

Số phức được biểu diễn dạng x + yj. Trong đó x là phần thực, y là phần ảo.

### -         **Phân số \(fraction\)**

Phân số thuộc thư viện faction có dạng: Fraction\(&lt;Tử\_số&gt;, &lt;Mẫu\_số&gt;\). Trước khi sử dụng cần import thư viện fraction.

Ví dụ:

```python
a = 1234567890123456789 
    # print(a) cho kết quả là 1234567890123456789
b = 0.1234567890123456789 
    # print(b) cho kết quả là 0.123456789012345678
c = 1+2j 
    # print(c) cho kết quả là 1+2j
```

Lưu ý: kết quả print\(b\) đã bị cắt bớt về 15 chữ số trong phần thập phân.

## 2. Kiểu xâu \(str\)

Trong Python, string là một dãy các ký tự Unicode. Unicode bao gồm mọi ký tự trong tất cả các ngôn ngữ và mang lại tính đồng nhất trong mã hóa.

Một xâu được đặt trong cặp nháy đơn hoặc nháy kép ', ". Xâu trên nhiều dòng được đặt trong cặp ba nháy đơn hoặc 3 nháy kép ''', """.

Ví dụ:

```python
s = 'This is a string'
print(s)
s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)
```

Output:

> This is a string
>
> This is a string
>
> A multiline
>
> string

Một xâu trong Python được đánh chỉ sổ cho từng ký tự bắt đầu từ 0. Để truy cập vào phần tử string ta sử dụng tham số chỉ số trong ngặc vuông \[\]

Ví dụ:

```python
s = 'Hello world!'
print("s[4] = ", s[4])
print("s[6:11] = ", s[6:11])
```

Output:

> s\[4\] =  o
>
> s\[6:11\] =  world

## 3. Kiểu Danh sách \(list\)

Trong Python, list được biểu diễn bằng dãy các giá trị, được phân tách nhau bằng dấu phẩy, nằm trong dấu \[\]. Các danh sách có thể chứa nhiều mục với kiểu khác nhau, nhưng thông thường là các mục có cùng kiểu.

List là kiểu dữ liệu tương tự kiểu mảng trong Pascal.

Kiểu list có dạng:

```python
a = [1, 2.2, 'python']
```

Các phần tử trong list có chỉ số bắt đầu từ 0. Ta có thể gọi 1 hay nhiều phần tử trong list bằng các đối số trong ngoặc \[\].

Ví dụ:

```python
a = [5,10,15,20,25,30,35,40]
print("a[2] = ", a[2])
print("a[0:3] = ", a[0:3])
print("a[5:] = ", a[5:])
```

Output:

> a\[2\] =  15
>
> a\[0:3\] =  \[5, 10, 15\]
>
> a\[5:\] =  \[30, 35, 40\]

Ta có thể thay đổi giá trị của phần tử trong list bằng cách gán giá trị mới vào phần tử.

Ví dụ:

```python
a = [1, 2, 3]
a[2] = 4 # gán 4 vào phần tử a[2]
print(a)
```

Output: `[1, 2, 4]`

### **List trong list**

Bạn cũng có thể tạo các list lồng nhau \(danh sách chứa trong danh sách\).

Với list lồng nhau ta có thể xử lý dữ liệu dạng mảng đa chiều trong C++ và Pascal.

Ví dụ:

```python
# nested list, dạng phức hợp
my_list = ["mouse", [8, 4, 6], ['a']]
# nested list, dạng mảng 2 chiều
my_list = [[1, 2, 3], [2, 3, 4]]
```

Trên đây chỉ là một số kiến thức cơ bản về list. Chúng ta tạm thời dừng lại ở đây để tiếp cận các kiến thức khác trước khi tìm hiểu sâu hơn về list trong một bài khác.

## 4. Kiểu Tuple

Kiểu tube giống như list, chỉ khác ở chỗ tuple không cho gán giá trị cho phần tử trong tuple \(không cho thay đổi giá trị các phần tử của tuple\).

Các phần tử của tuple được đặt trong dầu ngoặc đơn.

```python
t = (5,'program', 1+3j)
```

Truy xuất phần tử của tube bằng cách sử dụng ngoặc vuông với đối số là chỉ số phần tử:

```python
t = (5,'program', 1+3j)
print("t[1] = ", t[1])
print("t[1:3] = ", t[1:3])
```

Output:

> t\[1\] =  program
>
> t\[1:3\] =  \('program', \(1+3j\)\)

## 5. Kiểu Set

Set tương tự như list nhưng các phần tử là khắc biệt và không có thứ tự, không cho truy xuất từng phần tử trong set.

Ví dụ:

```python
a = {1,2,2,3,3,3}
print(a)
```

Output:

> {1, 2, 3}

## 6. Kiểu Dictionary \(dict\)

Dictionary là tập hợp các cặp khóa giá kèm trị không có thứ tự. Nó thường được sử dụng khi chúng ta có một số lượng lớn dữ liệu. Các dictionary được tối ưu hóa để trích xuất dữ liệu với điều kiện bạn phải biết được khóa để lấy giá trị.

Ví dụ:

```python
d = {1:'value','key':2}
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);
```

Output:

> d\[1\] =  value
>
> d\['key'\] =  2

## 7. Ép kiểu  - chuyển đổi kiểu dữ liệu

Chúng ta có thể chuyển đổi giữa các kiểu dữ liệu khác nhau bằng cách sử dụng hàm chuyển đổi kiểu khác nhau như int\(\) \(kiểu số nguyên\), float\(\) số thập phân, str\(\) chuỗi,...

Ví dụ:

```python
float(5)        # chuyển 5 về kiểu số thực => 5.0
int(10.6)       # chuyển 10.6 về kiểu số nguyên => 10
int(-10.6)      # chuyển -10.6 về kiểu số nguyên => -10
float('2.5')    # chuyển xâu ‘2.5’ về kiểu số thực => 2.5
str(25)         # chuyển số 25 về kiểu xâu => ‘25’
set([1,2,3])    # chuyển list về kiểu set => {1, 2, 3}
tuple({5,6,7})  # chuyển set về kiểu tuple => (5, 6, 7)
list('hello')   # chuyển xâu về kiểu list => ['h', 'e', 'l', 'l', 'o']
dict([[1,2],[3,4]])     # chuyển list về kiểu dict => {1: 2, 3: 4}
dict([(3,26),(4,44)])   # chuyển tuple về kiểu dict => {3: 26, 4: 44}
```

Chuyển đổi về dict đòi hỏi các giá trị kiểu khác phải theo cặp.

