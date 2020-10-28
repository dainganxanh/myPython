# Bài 10. Cấu trúc rẽ nhánh if…else

## 1. Câu lệnh if

Cú pháp:

```text
if <điều kiện>:
    <câu/khối lệnh thực thi khi điều kiện đúng>
```

Lưu ý: Câu lệnh hoặc khối lệnh trong lệnh if phải được thụt đầu dòng như nhau.

Ví dụ:

```python

# If the number is positive, we print an appropriate message
num = 3
if num > 0:
    print(num, "là một số nguyên.")
print("Dòng này không liên quan đến lệnh if.")
num = -1
if num > 0:
    print(num, "là một số nguyên.")
print("Dòng này cũng không liên quan đến lệnh if.")# If the number is positive, we print an appropriate message
num = 3
if num > 0:
    print(num, "là một số nguyên.")
print("Dòng này không liên quan đến lệnh if.")
num = -1
if num > 0:
    print(num, "là một số nguyên.")
print("Dòng này cũng không liên quan đến lệnh if.")
```

Output:

> 3 là một số nguyên  
> Dòng này không liên quan đến lệnh if.  
> Dòng này cũng không liên quan đến lệnh if.

## 2. Câu lệnh if…else

Cú pháp:

```text
if <điều kiện>:
    <câu/khối lệnh thực thi khi điều kiện đúng>
else:
    <câu/khối lệnh thực thi khi điều kiện không đúng>
```

Ví dụ:

```text
num = 3
if num >= 0:
    print("Lớn hơn hoặc bằng 0.")
else:
    print("Số âm.")
```

Output: `Lớn hơn hoặc bằng 0.`

## 3. Câu lệnh if...elif...else

Cú pháp:

```python
if <điều kiện 1>:
    <câu/khối lệnh thực thi khi điều kiện 1 đúng>
if <điều kiện 2>:
    <câu/khối lệnh thực thi khi điều kiện 2 đúng>
else:
    <câu/khối lệnh thực thi khi các điều kiện trên không đúng>
```

Ví dụ:

```python
num = 3.4
if num > 0:
    print("Số dương.")
elif num == 0:
    print("Zero.")
else:
    print("Số âm.")
```

Output: `Số dương.`

## 4. Câu lệnh if lồng nhau

Ví dụ:

```python
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

Output 1:

`Enter a number: 5  
Positive number`

Output 2:

`Enter a number: -1  
Negative number`

Output 3:

`Enter a number: 0  
Zero`

