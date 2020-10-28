# Bài 15. Tham số hàm

## 1. Tham số

Xét ví dụ sau:

```python
def hello(name, msg):
    """Hàm in ra lời chào
    với tên và lời chào được nhập vào"""
    print("Xin chào", name + ', ' + msg)

hello("Python", "Có gì mới không?")
```

Output: `Xin chào Python, Có gì mới không?`

Ở ví dụ trên, hàm hello có 2 tham số là name và msg. Ở câu lệnh gọi hàm ta truyền vào tham số name = "Python", tham số msg = "Có gì mới không?"

Lời gọi hàm phải được truyền đủ tham số. Nếu ta truyền thiếu hoặc thừa tham số thì chương trình sẽ báo lỗi. Ví dụ khi ta gọi hàm như sau

```python
hello("Python")
```

Output: `TypeError: hello() missing 1 required positional argument: 'msg'`

## 2. Tham số mặc định

```python
def hello(name, msg="Có gì hay???"):
    """Hàm in ra lời chào"""
    print("Xin chào", name + ', ' + msg)

hello("Python", "Có gì mới không?")
hello("Python")    # không còn báo lỗi 
```

Output:

> Xin chào Python, Có gì mới không?  
> Xin chào Python, Có gì hay???

Như vậy, hàm có tham số mặc định thì khi gọi hàm ta có không truyền tham số hàm sẽ lấy giá trị mặc định   để thực thi.

_**Lưu ý:**_ Giá trị mặc định có thể gán cho tất cả các tham số của hàm. Nhưng nếu trong hàm có một tham số không được gán giá trị mặc định thì tất cả các tham số có gán giá trị mặc định phải được đặt sau tham số không có giá trị mặc định.

```python
def hello(name="tên gì đó", msg="Có gì hay???"): # hàm này OK
    ...
    
def hello(name="tên gì đó", msg):     # hàm này sẽ báo lỗi khi được gọi 
    ...
```



## 3. Tham số keywords

```python
def hello(name, msg="Có gì hay???"):
    """Hàm in ra lời chào"""
    print("Xin chào", name + ', ' + msg)

# 2 keyword arguments
hello(name = "Python",msg = "Bạn có khỏe không?")

# 2 keyword arguments (out of order)
hello(msg = "Bạn có khỏe không?",name = "Python") 

# 1 positional, 1 keyword argument
hello("Python", msg = "Bạn có khỏe không?") 
```

Output:

> Xin chào Python, Bạn có khỏe không?  
> Xin chào Python, Bạn có khỏe không?  
> Xin chào Python, Bạn có khỏe không?

## 4. Tham số tùy ý

Lệnh gọi hàm không giới hạn số lượng tham số truyền vào.

```python
def hello(*Names):
    for name in Names:
        print("Hello", name)

hello("Python", "C++", "Java", "Pascal")
```

Output:

> Hello Python  
> Hello C++  
> Hello Java  
> Hello Pascal

