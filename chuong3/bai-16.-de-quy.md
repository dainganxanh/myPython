# Bài 16. Đệ quy

## Hàm đệ quy

Một hàm được gọi là đệ quy khi nó tự gọi lại chính nó nhiều lần đến khi vấn đề được giải quyết. 

Một hàm đệ quy cần phải có điều kiện chấm dứt đề dừng việc tự gọi lại chính nó. Hàm đệ quy chấm dứt khi mỗi lần gọi đệ quy thì số giải pháp của vấn đề được giảm bớt và tiến gần đến điều kiện cơ sở. Một điều kiện cơ sở là điểm mà ở đó vấn đề được giải quyết và không cần đệ quy thêm lần nào nữa.

Sau đây là một ví dụ về một hàm đệ quy để tìm giai thừa của một số nguyên.

Giai thừa của một số là tích của tất cả các số nguyên từ 1 đến số đó. Ví dụ, giai thừa của 6 \(được ký hiệu là 6!\) Là `1 * 2 * 3 * 4 * 5 * 6 = 720`.

```python
def giaithua(x):
    """Hàm tính giai thừa của một số nguyên"""
    if x == 1:
        return 1
    else:
        return (x * giaithua(x-1))

num = 6
print(f"Giai thừa của {num} là {giaithua(num)}")
```

Khi thực hiện gọi hàm giaithua trên đây với tham số truyền vào là num= 6 thì các bước thực hiện sẽ lần lượt như sau:

> 6 \* giaithua\(5\)                             \# gọi hàm lần thứ nhất  
> 6 \* 5 \* giaithua\(4\)                       \# gọi lần 2  
> 6 \* 5 \* 4 \* giaithua\(3\)                 \# gọi lần 3  
> 6 \* 5 \* 4 \* 3 \* giaithua\(2\)           \# gọi lần 4  
> 6 \* 5 \* 4 \* 3 \* 2 \* giaithua\(1\)     \# gọi lần 5 - gặp điều kiện cơ sở \(x=1\)  
> 6 \* 5 \* 4 \* 3 \* 2 \* 1                      \# giá trị trả về sau lần gọi cuối

Python mặc định độ duyệt sâu tối đa của hàm đệ quy là 1000 lần. Nếu tự gọi vượt quá số lần cho phép chương trình không trả về kết quả mà báo lỗi `RecursionError: maximum recursion depth exceeded`.

### Ví dụ 2

Tính tổng dãy số nguyên a gồm n phần tử từ 1 đến n.

```python
def tong(n):
    if n == 1:
        return 1
    else:
        return n + tong(n-1)
    
n = 6
print(tong(n))
```

### Ví dụ 3

In dãy fibonacy

```python
def fb(x):
    if (x == 0 or x == 1):
        return x;
    else:
        return fb(x-1) + fb(x-2)
    
n = 10
for i in range(n+1):
    print(fb(i), end=' ')
```

### Ưu điểm của Đệ quy 

Đệ quy làm cho mã code gọn gàng, mạch lạc . 

Một nhiệm vụ phức tạp có thể được chia thành các bài toán con đơn giản hơn bằng cách sử dụng đệ quy. 

Việc tạo trình tự với đệ quy dễ dàng hơn so với việc sử dụng một số phép lặp lồng nhau.

### Nhược điểm của Đệ quy 

Đôi khi logic đằng sau đệ quy rất khó theo dõi. 

Cuộc gọi đệ quy rất tốn kém \(không hiệu quả\) vì chúng chiếm nhiều bộ nhớ và thời gian. 

Các hàm đệ quy rất khó gỡ lỗi.





