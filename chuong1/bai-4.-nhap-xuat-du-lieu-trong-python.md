# Bài 4. Nhập, xuất dữ liệu

## 1. In dữ liệu ra màn hình

Để in dữ liệu ra màn hình ta sử dụng câu lện print\(\). Ví dụ

```python
print('In dòng này ra màn hình ')
a = 5
print('Giá trị được gán cho a là', a)
input()
```

## 2. Nhập dữ liệu từ bàn phím

Để nhận một giá trị được nhập từ bàn phím ta sử dụng lệnh input\(\). Ví dụ: Viết chương trình tính tổng 2 số nguyên được nhập từ bàn phím.

```python
num1 = int(input())
num2 = int(input())
sum = num1 + num2
print(sum)
input()
```

Ghi chú: mặc định, nếu không khai báo kiểu dữ liệu nhập vào thì Python sẽ nhận giá trị nhập từ bàn phím ở dạng xâu \(string\). Vì vậy dể nhập số ta phải khai báo kiểu dữ liệu trước khi nhập như câu lệnh số 1 và câu lệnh số 2 ở chương trình trên.

## 3. Định dạng dữ liệu và thông báo

Hiện thông báo khi nhập và in:

```python
num1 = input('Nhập số thứ nhất: ')
num2 = input('Nhập số thứ hai: ')
sum = int(num1) + int(num2)
print('Tổng của hai số vừa nhập là:', sum)
print('Tổng của {0} và {1} là {2}'.format(num1, num2, sum))
print('Tổng của {1} và {0} là {2}'.format(num1, num2, sum))
input()
```

Hãy xem sự khác nhau giữa 3 lệnh print\(\) trên đây khi chạy chương trình. Câu lệnh print thứ 2 và 3 có sử dụng định dạng dữ liệu để lồng vào thông báo.

Kết quả chạy chương trình:

> Nhập số thứ nhất: 5  
> Nhập số thứ hai: 9  
> Tổng của hai số vừa nhập là: 14.0  
> Tổng của 5 và 9 là 14.0  
> Tổng của 9 và 5 là 14.0

