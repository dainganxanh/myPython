# Bài 26. Dữ liệu kiểu dictionary

Kiểu từ điển \(dict\) trong Python là một tập hợp các phần tử không có thứ tự. Mỗi phần tử của dict có một cặp khóa : giá trị \(key : value\).

Dict được khai báo nằm trong cặp ngoặc nhọn giống như set {}. Việc truy xuất giá trị phần tử sẽ được thực hiện thông qua khóa \(key\).

## Khởi tạo dict

```python
d = {}

d = {1: 'apple', 2: 'ball'}

d = {'name': 'John', 1: [2, 4, 3]}

d = dict({1:'apple', 2:'ball'})

d = dict([(1,'apple'), (2,'ball')])
```

## Truy cập phần tử dict

Truy cập phần tử dict thông qua key trong cặp ngoặc vuông \[\] hoặc sử dụng phương thức get\(\).

Ví dụ:

```python
d = {'name': 'Jack', 'age': 26}

print(d['name']) # Jack

print(d.get('age')) # 26

print(d.get('address')) # None (truy cập phần tử không tồn tại)

print(d['address']) # Báo lỗi KeyError
```

## Thêm, sửa, xóa phần tử dict

### Thêm, sửa

```python
d = {'name': 'Jack', 'age': 26}

d['age'] = 27        # gán giá trị cho phần tử có khóa là age

print(d)             # {'age': 27, 'name': 'Jack'}

d['dc'] = 'Downtown' # thêm phần tử mới cho dict

print(d)             # {'dc': 'Downtown', 'age': 27, 'name': 'Jack'}
```

### Xóa

```python
# tạo dict
dbp = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# xóa phần tử theo key, trả về giá trị tương ứng
print(dbp.pop(4))     # 16
print(dbp)            # {1: 1, 2: 4, 3: 9, 5: 25}

# xóa phần tử cuối, trả về cặp (key,value)
print(dbp.popitem())   # (5, 25)
print(dbp)             # {1: 1, 2: 4, 3: 9}

dbp.clear()            # Xóa hết phần tử
print(dbp)             # {}

del dbp                # xóa biến 
```

## Các phương thức với dict

| Method | Chú thích |
| :--- | :--- |
| [clear\(\)](https://www.programiz.com/python-programming/methods/dictionary/clear) | Xóa hết các phần tử |
| [copy\(\)](https://www.programiz.com/python-programming/methods/dictionary/copy) | Trả về bản sao của dict |
| [fromkeys\(seq\[, v\]\)](https://www.programiz.com/python-programming/methods/dictionary/fromkeys) | Gán v làm giá trị mặc định cho các key khi khởi tạo dict. \(v mặc định = `None`\). |
| [get\(key\[,d\]\)](https://www.programiz.com/python-programming/methods/dictionary/get) | Trả về giá trị của key. Nếu key không tồn tại thì trả về d \(mặc định là `None`\). |
| [items\(\)](https://www.programiz.com/python-programming/methods/dictionary/items) | Trả về cặp \(key, value\)  |
| [keys\(\)](https://www.programiz.com/python-programming/methods/dictionary/keys) | Trả về danh sách các key của dict. |
| [pop\(key\[,d\]\)](https://www.programiz.com/python-programming/methods/dictionary/pop) | Xóa phần tử theo key và trả về giá trị phần tử đó \(value\) Hoặc trả về d nếu key cần xóa không tồn tại \(nếu bỏ trống d thì sẽ báo lỗi `KeyError`\). |
| [popitem\(\)](https://www.programiz.com/python-programming/methods/dictionary/popitem) | Xóa và trả về cặp \(**key, value**\). Lỗi `KeyError` nếu dict rỗng. |
| [setdefault\(key\[,d\]\)](https://www.programiz.com/python-programming/methods/dictionary/setdefault) | Trả về giá trị tương ứng nếu key có trong dict. Nếu không sẽ chèn key với giá trị d và trả về d \(mặc định là `None`\). |
| [update\(\[other\]\)](https://www.programiz.com/python-programming/methods/dictionary/update) | Cập nhật từ điển với các cặp key/value từ các cặp key/value khác, ghi đè các key hiện có. |
| [values\(\)](https://www.programiz.com/python-programming/methods/dictionary/values) | Trả về danh sách các value của dict. |

```python
diem = {}.fromkeys(['Toán', 'Văn', 'Anh'], 0)

print(diem)         # {'Toán': 0, 'Văn': 0, 'Anh': 0}

for item in diem.items():
    print(item)
                    ''' 
                    ('Toán', 0)
                    ('Văn', 0)
                    ('Anh', 0)
                    '''
print(list(sorted(diem.keys()))) # ['Anh', 'Toán', 'Văn']
```

## Dictionary Comprehension

Comprehension với dict tương tự như với list, tuple, set. 

```python
bp= {x: x*x for x in range(6)}

print(bp)
```

```python
bpl = {x: x*x for x in range(11) if x % 2 == 1}

print(bpl)
```

## Hàm dựng sẵn cho dict

Các hàm dựng sẵn thường dùng cho dict gồm all\(\), any\(\), len\(\), sorted\(\), ... 

```python
d = {0: 11, 1: 20, 3: 9, 5: 25, 7: 49, 9: 81}

print(all(d))     # False
print(any(d))     # True
print(len(d))     # 6
print(sorted(d))  # [0, 1, 3, 5, 7, 9]
```

## Thao tác khác

### Kiểm tra key chứa trong dict

Dùng từ khóa in để kiểm tra xem có tồn tại key nào đó trong dict không \(không phải kiểm tra giá trị\)

```python
d = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in d) # True
print(2 not in d) # True
print(49 in d) # False
```

### Lặp theo phần tử dict

```python
d = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in d:
    print(d[i])
```

Output: `1  
9  
25  
49  
81`

