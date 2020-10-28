# Bài 18. Biến toàn cục và cục bộ

Biến cục bộ \(local\) là biến có hiệu lực trong nội bộ của hàm. Biến toàn cục \(global\) là biến có hiệu lực trong toàn chương trình - tuy nhiên nó cần được khai báo để có thể hoạt động trong thân hàm. 

## 1. Biến toàn cục \(global\)

Ví dụ 1

```python
x = "biến toàn cục - global"

def foo():
    print("x trong hàm:", x)

foo()
print("x ngoài hàm:", x)
```

Output:

`x trong hàm: biến toàn cục - global  
x ngoài hàm: biến toàn cục - global`

Xét ví dụ 2

```python
x = "biến global "

def foo():
    x = x * 2
    print(x)

foo()
```

Output: `Báo lỗi "UnboundLocalError: local variable 'x' referenced before assignment"`

Biến x được khai báo ngoài hàm và được gán giá trị là "biến global". Tuy nhiên, câu lệnh ở dòng 4 có sử dụng biến x trong hàm \(lúc này x được coi làm một local và chưa được khai báo\) nên phát sinh lỗi.

Để khắc phục lỗi này ta có thể khai báo biến x trong hàm là biến toàn cục với keyword global như sau:

```python
x = "biến global "

def foo():
    global x
    x = x * 2
    print(x)

foo()
```

Ouput: `biến global biến global`

## 2. Biến cục bộ \(local\)

Thông thường, chúng ta khai báo một biến bên trong hàm để tạo một biến cục bộ. Ví dụ như sau:

```python
def foo():
    y = "local"
    print(y)

foo()
```

Output: `local`

Tuy nhiên, chương trình sau đây sẽ báo lỗi

```python
def foo():
    y = "local"

foo()
print(y)
```

Output: `NameError: name 'y' is not defined`

Nguyên nhân: Chương trình trên gọi biến y ngoài hàm trong khi biến y là một biến local \(chỉ có phạm vi hoạt động trong hàm, biến y sẽ bị hủy khi thoát khỏi hàm foo\(\)\)

## 3. Biến không cục bộ \(nonlocal\)

Sử dụng khái niệm global, local trong trường hợp hàm trong hàm. Xét ví dụ dau:

```python
x = 5
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print(x)
```

Output: `inner: nonlocal  
outer: nonlocal  
5`

_**Giải thích:**_   
Vì inner là một hàm trong hàm nên để biến x trong hàm inner\(\) có thể hoạt động ngoài thân hàm inner\(\) thì phải khai báo với từ khóa nonlocal. Lúc này x trong hàm inner\(\) chính là x của hàm outter\(\).

## 4. Ví dụ tổng hợp

### Ví dụ 4.1

```python
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
```

Output: `global global   
local`

### Ví dụ 4.2

```python
x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)
```

Output: `local x: 10  
global x: 5`

Ở ví dụ này biến global và local cùng có tên là x. Tuy nhiên do phạm vi hoạt động của global và local là rạch ròi nên chương trình là hợp lệ và hoạt động bình thường.

### Ví dụ 4.3

Xem xét kỹ ví dụ sau để thấy phạm vi biến global, local và nonlocal

```python
x = 25
y = '- hai lăm'
def foo():
    x = 20
    y = '- hai mươi'
    def bar():
        nonlocal x
        x = 35
        
        global y
        y = '- ba lăm'

    print("\t x - y trước khi gọi hàm bar: \t", x, y)
    bar()
    print("\t x - y sau khi gọi hàm bar: \t", x, y)

print('x - y ngoài hàm,trước khi gọi hàm foo: \t', x, y)
foo()
print("x - y ngoài hàm, sau khi gọi foo: \t", x, y)
```

Output:

`x - y ngoài hàm,trước khi gọi hàm foo: 	 25 - hai lăm  
	 x - y trước khi gọi hàm bar: 	 20 - hai mươi  
	 x - y sau khi gọi hàm bar: 	 35 - hai mươi  
x - y ngoài hàm, sau khi gọi foo: 	 25 - ba lăm`

## 

