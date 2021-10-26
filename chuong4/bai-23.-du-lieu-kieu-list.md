# Bài 23. Dữ liệu kiểu list

List là một trong những kiểu dữ liệu được sử dụng thường xuyên nhất và rất linh hoạt trong Python.

## Khởi tạo list

```python
# list rỗng
my_list = []

# list số nguyên
my_list = [1, 2, 3]

# list hỗn hợp
my_list = [1, "Hello", 3.4]

# list lồng nhau
my_list = ["mouse", [8, 4, 6], ['a']]
```

## Truy cập phần tử list

```python
my_list = ['H', 'ọ', 'c', ' ', 'P', 'y', 't', 'h', 'o', 'n']

print(my_list[0])        # Output: H
print(my_list[2])        # Output: c
print(my_list[4])        # Output: p

n_list = ["Happy", [2, 0, 1, 5]]    # list lồng nhau

print(n_list[0][1])        # Output: a
print(n_list[1][3])        # Output: 5
```

Lưu ý: chỉ số để truy xuất phần tử list phải là số nguyên

## Truy cập phần tử list theo chỉ số âm

```python
my_list = ['H', 'ọ', 'c', ' ', 'P', 'y', 't', 'h', 'o', 'n']

print(my_list[-1])    # Output: n
print(my_list[-5])    # Output: y
```

## Cắt đoạn list

```python
my_list = ['H', 'ọ', 'c', ' ', 'P', 'y', 't', 'h', 'o', 'n']

print(my_list[2:5])     # ['c', ' ', 'P']
print(my_list[:-5])     # ['H', 'ọ', 'c', ' ', 'P']
print(my_list[5:])     # ['y', 't', 'h', 'o', 'n']
print(my_list[:])     # ['H', 'ọ', 'c', ' ', 'P', 'y', 't', 'h', 'o', 'n']
```

Lưu ý: tham số cắt đoạn \[a:b] được lấy từ phần tử có chỉ số a đến phần tử trước chỉ số b.&#x20;

## Thêm, sửa phần tử list

### Thay đổi giá trị phần tử&#x20;

```python
a = [2, 4, 6, 8]

# đổi giá trị phần tử a[0]    
a[0] = 1            
print(a)        # [1, 4, 6, 8]

# đổi giá trị phần tử a[1] đến a[3]
a[1:4] = [3, 5, 7]  
print(a)         # [1, 3, 5, 7]
```

### Thêm phần tử vào list

Dùng append() và extend()

```python
ma = [0, 9, 1, 8, 9, 1, 8]

ma.append(4)
print(ma)         # [0, 9, 1, 8, 9, 1, 8, 4]

ma.extend([4, 7])
print(ma)         # [0, 9, 1, 8, 9, 1, 8, 4, 4, 7]
```

Dùng toán tử +, \*

```python
ma = [0, 9, 1, 8, 9, 1, 8]

ma += [4,4,7]
print(ma)         # [0, 9, 1, 8, 9, 1, 8, 4, 4, 7]

mb = 'Happy! '
print(mb * 5)     # Happy! Happy! Happy! Happy! Happy!
```

Dùng phương thức insert()

```python
ma = [1, 9]

ma.insert(1,3)
print(ma)         # [1, 3, 9]

ma[2:2] = [5, 7]
print(ma)         # [1, 3, 5, 7, 9]
```

## Xóa phần tử list

```python
ma = ['P', 'y', 't', 'h', 'o', 'n', '3']

del ma[2]    # delete one item
print(ma)    # ['P', 'y', 'h', 'o', 'n', '3']

del ma[1:5]   # delete multiple items
print(ma)     # ['P', '3']

del ma        # delete entire list
# Nếu print(ma) sẽ cho lỗi: List not defined
```

Ta có thể sử dụng các phương thức remove(), pop(), clear() để xóa phần tử list.&#x20;

```python
ma = ['P', 'y', 't', 'h', 'o', 'n', '3']

ma.remove('y')
print(ma)            # Output: ['P', 't', 'h', 'o', 'n', '3']
print(ma.pop(1))     # Output: 't'
print(ma)            # Output: ['P', 'h', 'o', 'n', '3']
print(ma.pop())      # Output: '3'
print(ma)            # Output: ['P', 'h', 'o', 'n']

ma.clear()
print(ma)            # Output: []
```

Hoặc ta có thể xóa phần tử list bằng cách gán list rỗng cho phần tử muốn xóa&#x20;

```python
ma = ['P', 'y', 't', 'h', 'o', 'n', '3']

ma[2:4] = []
print(ma)     # ['P', 'y', 'o', 'n', '3']
```

## Phương thức (list method)

Phương thức trong Python được gọi bởi dấu chấm và tên phương thức sau tên biến. Có dạng list.method(). Các phương thức xử lý list gồm:

`append() - thêm phần tử`\
`extend() - nối list`\
`insert() - chèn phần tử theo chỉ số `\
`remove() - xóa một phần tử list`\
`pop() - Xóa và trả về chỉ số phần tử vừa xóa`\
`clear() - Xóa hết các phần tử của list -> trả về list rỗng`\
`index() - Trả về chỉ số của phần tử đầu tiên có giá trị như tham số`\
`count() - Đếm số phần tử có giá trị như tham số`\
`sort() - Sắp xếp thành list tăng dần`\
`reverse() - Đảo chiều phần tử list`\
`copy() - Sao chép list`

Ví dụ:

```python
ma = [9, 1, 8, 9, 1, 8, 4]

print(ma.index(9))    # Output: 0
print(ma.count(8))    # Output: 2

ma.sort()
print(ma)    # Output: [1, 1, 4, 8, 8, 9, 9]

ma.reverse()
print(ma)    # Output: [9, 9, 8, 8, 4, 1, 1]
```

## List Comprehension

Chưa biết nên dịch thuật ngữ list comprehension là gì nhưng đây là một cách ngắn gọn và riêng có của Python để tạo một list từ list đã có. Xét một vài ví dụ để xem cách hoạt động của list comprehension dưới đây:

```python
pow2 = [2 ** x for x in range(10)]
print(pow2)    # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)    # [64, 128, 256, 512]

odd = [x for x in range(20) if x % 2 == 1]
print(odd)    # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

a = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(a)    # ['Python Language', 'Python Programming', 'C Language', 'C Programming']
```

## Thao tác khác

### Kiểm tra phần tử chứa trong list

```python
ma = ['P', 'y', 't', 'h', 'o', 'n', '3']

print('h' in ma)    # Output: True

print('a' in ma)    # Output: False

print('c' not in ma)    # Output: True
```

### Lặp theo phần tử list

```python
mau = ['xanh','đỏ', 'vàng']

for x in ['apple','banana','mango']:
    print("I like",x)

for i in mau:
    print('Tôi thích màu', i)
```

Output: `I like apple`\
`I like banana`\
`I like mango`\
`Tôi thích màu xanh`\
`Tôi thích màu đỏ`\
`Tôi thích màu vàng`

## Thao tác tạo list bổ sung

Tạo list đơn có n phần tử

```python
n = 5
ma = [None]*n
print(ma)
```

Output: \[None, None, None, None, None]

Tạo nested list dạng mảng 2 chiều có c cột và d dòng

```python
c = 5
d = 3
ma = [[None for x in range(c)] for x in range(d)]
```

Output: \[\[None, None, None, None, None], \[None, None, None, None, None], \[None, None, None, None, None]]

