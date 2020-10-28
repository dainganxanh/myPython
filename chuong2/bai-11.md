# Bài 11. Cấu trúc lặp với for

## 1. Vòng lặp for

Cú pháp:

```python
for <biến lặp> in <biến liên tục>:
    <câu/khối lệnh thực thi bằng số phần tử của biến liên tục lần>
```

Biến liên tục có thể là list, tuple, string.

Ví dụ:

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for n in numbers:
        sum += n  # hoặc sum = sum+n
print("Tổng = ", sum)   
```

Output: `Tổng = 48`

## 2. Hàm range\(\)

Hàm range\(\) để tạo ra một dãy số. Ví dụ, range\(10\) sẽ tạo một dãy số liên tục từ 0 đến 9 \(10 số\).

Hàm range\(số bắt đầu, số kết thúc, khoảng cách giữa hai số\) được sử dụng để tạo dãy số tùy chỉnh. Nếu không đặt khoảng cách giữa hai số thì Python sẽ hiểu mặc định nó bằng 1.

Hàm range\(\) không lưu tất cả các giá trị trong bộ nhớ mà nó lưu giá trị bắt đầu, giá trị kết thúc và khoảng cách giữa hai số từ đó tạo ra số tiếp theo trong dãy.

Để range\(\) xuất ra tất cả các giá trị, bạn cần sử dụng đến hàm list\(\) giống như ví dụ dưới đây:

```python
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3))) # dãy từ 2 đến 20, mỗi phần tử cách nhau 3 đơn vị
```

Output:

> range\(0, 10\)  
> \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]  
> \[2, 3, 4, 5, 6, 7\]  
> \[2, 5, 8, 11, 14, 17\]

Dùng hàm range\(\) trong lệnh for:

```python
# Ví dụ này có dùng hàm len() để lấy độ dài của list
biends = ['pop', 'rock', 'jazz']
for i in range(len(biends)):
        print("I like", biends[i])
```

Output:

> I like pop  
> I like rock  
> ​I like jazz

## 3. Vòng lặp for else

Ví dụ:

```python
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")
```

Output:

> 0  
> 1  
> 5  
> No items left.

Sử dung break\(\) để thoát khỏi vòng lặp

```python
ten_hs = input('Nhập tên học sinh: ')
diem = {'Nam': 90, 'Anh': 99, 'Tan': 77}
for n in diem:
    if n == ten_hs:
        print(diem[n])
        break
else:
    print('Không tìm thấy tên học sinh vừa nhập.')
input()
```

Output 1: Nhập vào: Hanh

`Không tìm thấy tên học sinh vừa nhập.`

Output 2: Nhập vào: Anh

`99`

### **Bài tập vận dụng:**

Cho file input.txt gồm 2 dòng:

Dòng 1: gồm một số nguyên \(n &lt; 100\).

Dòng 2: Dãy a gồm n + 2 phần tử, mỗi phần tử là một ký tự cách nhau bởi 1 khoảng trắng.

**Yêu cầu:**

- Đọc n phần tử đầu tiên của dãy a và ghi vào file output.txt.

- Tính tổng các phần tử và ghi vào dòng thứ 2.

`Hướng dẫn:  
            Chuyển xâu có dạng: 1 2 3 4 5 thành list có dạng [1,2,3,4,5]  
            a = ‘1 2 3 4 5’  
            li = list(a.split(‘ ‘)`

