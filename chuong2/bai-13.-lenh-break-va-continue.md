# Bài 13. Lệnh break và continue

Lệnh break và continue dùng để xử lý trong trường hợp muốn thoát khỏi vòng lặp với một điều kiện ngoài điều kiện chung của vòng lặp bình thường.

Ví dụ sử dụng break:

```python
for val in "Học để biết":
    if val == "b":
        break
    print(val)
print("Kết thúc.")
input()
```

Output: Chương trình gặp chữ “b” sẽ thoát khỏi vòng lặp

`H  
ọ  
c  
đ  
ể  
Kết thúc.`

Ví dụ sử dụng continue:

```python
for val in "Học để biết":
    if val == " ":
        continue
    print(val)
print("Kết thúc.")
input()
```

Output: chương trình gặp khoảng trắng sẽ bỏ qua để thực thi tiếp vòng lặp

`H  
ọ  
c  
đ  
ể  
b  
i  
ế  
t  
Kết thúc.`

Ngoài ra còn có lệnh pass dùng để thoát khỏi một hàm hay vòng lặp \(không thực thi hàm hay vòng lặp đó trong chương trình.

Ví dụ:

```python
for val in sequence:
    pass
# Hoặc
def function(args):
    pass
# Hoặc
class Example:
    pass
```



