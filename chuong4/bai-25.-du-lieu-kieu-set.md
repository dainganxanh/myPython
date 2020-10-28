# Bài 25. Dữ liệu kiểu set

Set là một tập hợp các phần tử không có thứ tự. Mọi phần tử trong set là duy nhất \(không trùng lặp\) và bất biến \(không thể thay đổi\). Phần tử của set có thể có kiểu dữ liệu bất kỳ trừ list và chính nó.

## Khởi tạo set

```python
s1 = set([1,2,3,4])
s2 = {3, 4, 5}
print(s1)
print(s2)

ms = {1.0, "Hello", (1, 2, 3)}
print(ms)
```

Xét thêm các ví dụ sau để thấy set không chứa phần tử trùng lặp.

```python
s = {1, 2, 3, 4, 3, 2}
print(s)                # Output chỉ còn: {1, 2, 3, 4}

s = set([1, 2, 3, 2])   
print(s)                # {1, 2, 3}
```

Lưu ý: Ta không thể khởi tạo một set rỗng như cách làm với list và tuple. Ví dụ:

```python
s = {}
print(s)
print(type(s))    # <class 'dict'> - lúc này Python nhận kiểu dict

s = set({})
print(s)
print(type(s))    # <class 'set'>
```

## Thêm, ~~sửa~~, xóa phần tử set

### Thêm

```python
s = {1, 3}
print(s)

# s[0]  # bỏ comment dòng 4 này sẽ phát sinh lỗi
        #vì set không cho truy cập theo chỉ số

s.add(2)
print(s) # {1, 2, 3}

s.update([2, 3, 4])
print(s) # Output: {1, 2, 3, 4}

s.update([4, 5], {1, 6, 8})
print(s) # Output: {1, 2, 3, 4, 5, 6, 8}
```

### Xóa

Sử dụng phương thức discard\(\) và remove\(\). Lưu ý phương thức remove\(\) sẽ không hoạt động nếu phần tử chỉ định không tồn tại trong set.  

```python
s2 = {1, 3, 4, 5, 6}

s2.discard(4)     # xóa bỏ một phần tử bằng discard
print(s2)         # {1, 3, 5, 6}

s2.remove(6)      # xóa một phần tử bằng remove
print(s2)         # {1, 3, 5}

s2.discard(2)
print(s2)         # {1, 3, 5}
s2.remove(2)      # Báo lỗi KeyError vì phần tử không tồn tại
```

Dùng phương thức pop\(\), clear\(\)

```python
s = set("HelloWorld")
print(s)          # xem kỹ output nhé !

print(s.pop())    # phần tử đầu tiên của set

s.pop()           # xóa thêm một phần tử 
print(s)    

s.clear()
print(s)          # set rỗng: set()
```

## Các phép toán trên set

Các phép toán trên set chính là các phép toán trên tập hợp. Xét ví dụ sau:

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

U = A | B    # phép hợp
print(U)     # {1, 2, 3, 4, 5, 6, 7, 8}

I = A & B    # phép giao
print(I)     # {4, 5}

D = A-B      # phép hiệu
print(D)     # {1, 2, 3}

SD = A^B     # hiệu của hợp và giao
print(SD)    # {1, 2, 3, 6, 7, 8}
```

## Phương thức của set 

| Phương thức | Chú giải |
| :--- | :--- |
| [add\(\)](https://www.programiz.com/python-programming/methods/set/add) | Cộng thêm phần tử |
| [clear\(\)](https://www.programiz.com/python-programming/methods/set/clear) | Xóa rỗng set |
| [copy\(\)](https://www.programiz.com/python-programming/methods/set/copy) | Sao chép set |
| [difference\(\)](https://www.programiz.com/python-programming/methods/set/difference) | Phần khác  \(phép - \) |
| [difference\_update\(\)](https://www.programiz.com/python-programming/methods/set/difference_update) | Trả về set đã xóa hết các phần tử giống set khác |
| [discard\(\)](https://www.programiz.com/python-programming/methods/set/discard) | Xóa bỏ phần tử đầu của set |
| [intersection\(\)](https://www.programiz.com/python-programming/methods/set/intersection) | Phần giao 2 set \(phép &\) |
| [intersection\_update\(\)](https://www.programiz.com/python-programming/methods/set/intersection_update) | Trả về phần giao 2 set |
| [isdisjoint\(\)](https://www.programiz.com/python-programming/methods/set/isdisjoint) | `True` nếu 2 set không có phần giao |
| [issubset\(\)](https://www.programiz.com/python-programming/methods/set/issubset) | `True` nếu set chứa trong set khác   |
| [issuperset\(\)](https://www.programiz.com/python-programming/methods/set/issuperset) | `True` nếu set có chứa một set khác |
| [pop\(\)](https://www.programiz.com/python-programming/methods/set/pop) | Xóa phần tử đầu của set \(sẽ báo lỗi nếu xóa phần tử không có trong set\) |
| [remove\(\)](https://www.programiz.com/python-programming/methods/set/remove) | Xóa phần tử của set \(sẽ báo lỗi nếu xóa phần tử không có trong set\) |
| [symmetric\_difference\(\)](https://www.programiz.com/python-programming/methods/set/symmetric_difference) | Trả về set là phần khác đối xứng của 2 xét khác |
| [symmetric\_difference\_update\(\)](https://www.programiz.com/python-programming/methods/set/symmetric_difference_update) | Trả về set là phần khác đối xứng của 2 set khác |
| [union\(\)](https://www.programiz.com/python-programming/methods/set/union) | Trả về phần hợp 2 set \(phép hợp \| \) |
| [update\(\)](https://www.programiz.com/python-programming/methods/set/update) | Trả về một set là hợp của 2 set |

## Hàm dựng sẵn cho set

Các hàm dựng sẵn như all\(\), any\(\), enumerate\(\), len\(\), max\(\), min\(\), sorted\(\), sum\(\), v.v. thường được sử dụng với các set để thực hiện các tác vụ khác nhau.

| Function | Description |
| :--- | :--- |
| [all\(\)](https://www.programiz.com/python-programming/methods/built-in/all) | `True` nếu tất cả các phần tử true \(hoặc set rỗng\). |
| [any\(\)](https://www.programiz.com/python-programming/methods/built-in/any) | `True` nếu set có phần tử True. `False` nếu set rỗng |
| [enumerate\(\)](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Trả về một đối tượng liệt kê. Nó chứa chỉ số và giá trị cho tất cả các phần tử của set dưới dạng từng cặp.   |
| [len\(\)](https://www.programiz.com/python-programming/methods/built-in/len) | Số lượng phần tử của set |
| [max\(\)](https://www.programiz.com/python-programming/methods/built-in/max) | Phần tử lớn nhất của set |
| [min\(\)](https://www.programiz.com/python-programming/methods/built-in/min) | Phần tử nhỏ nhất của set |
| [sorted\(\)](https://www.programiz.com/python-programming/methods/built-in/sorted) | Trả về một list gồm các phần tử của set đã được sắp xếp |
| [sum\(\)](https://www.programiz.com/python-programming/methods/built-in/sum) | Tổng các phần tử của set |

## Frozenset

Frozenset có các đặc điểm của set nhưng không cho phép thêm-sửa-xóa phần tử. Nếu  tuple là dạng bất biến của list thì frozenset là dạng bất biến của set.

frozenset được khởi tạo bằng hàm frozenset\(\) và được hỗ trợ các phương thức như: copy\(\), difference\(\), intersection\(\), isdisjoint\(\), issubset\(\), issuperset\(\), symmetric\_difference\(\) and union\(\). 

Dĩ nhiên là không làm việc với remove\(\), discard...

Ví dụ

```python
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

U = A|B
I = A&B
D = A-B
DS = A^B

print(U) # frozenset({1, 2, 3, 4, 5, 6})
print(I) # frozenset({3, 4})
print(D) # frozenset({1, 2})
print(DS) # frozenset({1, 2, 5, 6})
```

## Thao tác khác

### Kiểm tra phần tử chứa trong set

```python
s = set("apple")

print('a' in s)         # True
print('p' not in s)     # False
```

### Lặp theo phần tử set

```python
for si in set("apple"):
    print(si) # in từng ký tự trong xâu apple
```

