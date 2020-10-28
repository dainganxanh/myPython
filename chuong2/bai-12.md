# Bài 12. Cấu trúc lặp với while

## 1. Vòng lặp while

Cú pháp

```python
while <điều kiện>:
    <câu/khối lệnh thực thi khi còn thỏa điều kiện>
```

Ví dụ:

```python
n = float(input("Nhập n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i +=1    # tăng biến đếm
print("Tổng: ", sum)
input()
```

Output: Bạn tự code để xem output nhé!

## 2. Vòng lặp while - else

Ví dụ:

```python
counter = 0
while counter < 3:
    print("Trong vòng lặp while")
    counter = counter + 1
else:
    print("Trong else, xảy ra khi điều kiện while không còn thỏa.")
```

Output:

`Trong vòng lặp while  
Trong vòng lặp while  
Trong vòng lặp while  
Trong else, xảy ra khi điều kiện while không còn thỏa.`

