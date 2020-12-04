# Mảng 2 chiều

## Đề bài

Cho file mang2.in như sau:
```
4 5
11 8 88 6
20 3 80 60
30 5 99 123
42 7 20 10
55 4 33 2020
```

Trong đó: Dòng thứ nhất là 2 số nguyên dương m, n cách nhau bở một khoảng trắng. 
n dòng tiếp theo, mỗi dòng gồm m số nguyên cách nhau bởi một khoảng trắng tạo thành mảng ma có m cột, n dòng. 

(mảng ma gồm 4 cột 5 dòng)

### Yêu cầu:
a. Đọc dữ liệu từ file mang2.in và in ra màn hình mảng ma.

b. Tính tổng đường chéo của mảng gồm m dòng đầu tiên của mảng ma. (tong = 11+3+99+10 = 123)

## Bài làm 

```Python
with open('mang2.IN') as fi:
	m,n = list(map(int,fi.readline().split()))
	ma = []
	for i in range(n):
		ma.append(list(map(int,fi.readline().split())))

## Câu a
for ai in ma:
	print(ai)

## Câu b
tong = 0
for i in range(m):
	for j in range(m):
		if i == j: tong += ma[i][j]
print(tong)		
```

## Giải thích:
### Đọc dữ liệu vào

`m,n = list(map(int,fi.readline().split()))` 

Lệnh này sử dụng phương thức .split() để tách xâu bởi các khoảng trắng tạo thành list. Như vậy, với dòng đầu của file mang2.in là `4 5` 
ta dùng lệnh `fi.readline().split())` và thu được dữ liệu vào là ['4', '5'].

Nếu ta dùng `m,n = fi.readline().split()` thì m được gán bằng '4' và n được gán bằng '5'. Lúc này m,n có kiểu dữ liệu là string.

Để chuyển dữ liệu từ string sang int ta có thể ép kiểu cho từng biến. Tuy nhiên như thế sẽ làm cho code dài và khó đọc. 
Trong bài này ta chuyển dữ liệu string sang int bằng hàm map(). `m,n = list(map(int,fi.readline().split()))`

Để dễ hiểu hơn về hàm map(). Xét ví dụ sau:

```Python
s = '1 2 3'
# Tách xâu s thành list a
ma = s.split() 
# in mảng a ta có: ['1', '2', '3']. (lúc này các phần tử là string)
print(ma)
# Chuyển các phần tử của mảng a thành kiểu int
ma = list(map(int,ma))
# in mảng a ta có: [1, 2, 3]
print(ma)
``` 

- [Đọc thêm về hàm map() tại đây](https://python.dainganxanh.com/phu-luc/ham-map)

- [Xem thêm ví dụ ép kiểu bằng map() tại đây](https://python.dainganxanh.com/phu-luc/ghi-chep-hau-truong#ep-kieu-phan-tu-list)
