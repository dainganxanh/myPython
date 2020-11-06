---
description: Python Objects and Classes
---

# Bài 33. Đối tượng và Lớp

Đối tượng \(Object\) chỉ đơn giản là một tập hợp các dữ liệu \(các biến\) và các phương thức \(các hàm\) hoạt động trên các dữ liệu đó. Và, lớp \(class\) là một kế hoạch chi tiết cho đối tượng.

Ta có thể hình dung class như một bản phác thảo \(nguyên mẫu\) của một ngôi nhà. Nó chứa tất cả các chi tiết về sàn nhà, cửa ra vào, cửa sổ,... Dựa trên những mô tả này, chúng ta sẽ xây \(hoặc in 3D\) các ngôi nhà và nhà ở đây chính là đối tượng.

### Khai báo một Class <a id="define"></a>

Cú pháp khai báo \(định nghĩa\) một Class như sau

```python
class TenClass:
    '''Đây là docstring để ghi chú cho class'''
    # các câu lệnh trong thân class 
```

Một class tạo ra một không gian tên cục bộ \(local namespace\) mới nơi tất cả các thuộc tính của nó được định nghĩa. Các thuộc tính có thể là dữ liệu hoặc hàm.

Ngoài ra còn có các thuộc tính đặc biệt được bắt đầu bằng dấu gạch dưới kép \_\_**. Ví dụ:** `__doc__`  cung cấp cho chúng ta docstring của class.

Ngay sau khi chúng ta định nghĩa một Class, một đối tượng lớp mới có cùng tên cũng được tạo. Đối tượng lớp này cho phép chúng ta truy cập các thuộc tính khác nhau cũng như khởi tạo các đối tượng mới của lớp đó.

```python
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: 'This is my second class'
print(Person.__doc__)
```

### Tạo đối tượng \(Object\) <a id="create"></a>

Đối tượng trong class có thể được sử dụng để truy cập các thuộc tính khác nhau và tạo các instance mới của lớp đó. Thủ tục để tạo một đối tượng tương tự như cách chúng ta gọi hàm.

```python
harry = Person()
```

Thao tác trên sẽ tạo một cá thể đối tượng mới có tên là harry. Chúng ta có thể truy cập các thuộc tính của đối tượng bằng tiền tố tên đối tượng. 

Các thuộc tính có thể là dữ liệu hoặc phương thức. Các phương thức của một đối tượng là các hàm tương ứng của lớp đó.

This means to say, since `Person.greet` is a function object \(attribute of class\), `Person.greet` will be a method object.

Điều này có nghĩa là, vì Person.greet là một đối tượng hàm \(thuộc tính của lớp\), nên Person.greet sẽ là một đối tượng phương thức.

```python
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()
```

**Output**

```python
<function Person.greet at 0x7fd288e4e160>
<bound method Person.greet of <__main__.Person object at 0x7fd288e9fa30>>
Hello
```

You may have noticed the `self` parameter in function definition inside the class but we called the method simply as `harry.greet()` without any [arguments](https://www.programiz.com/python-programming/function-argument). It still worked.

This is because, whenever an object calls its method, the object itself is passed as the first argument. So, `harry.greet()` translates into `Person.greet(harry)`.

In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method's object before the first argument.

For these reasons, the first argument of the function in class must be the object itself. This is conventionally called self. It can be named otherwise but we highly recommend to follow the convention.

Now you must be familiar with class object, instance object, function object, method object and their differences.

### Constructors in Python <a id="constructor"></a>

Class functions that begin with double underscore `__` are called special functions as they have special meaning.

Of one particular interest is the `__init__()` function. This special function gets called whenever a new object of that class is instantiated.

This type of function is also called constructors in Object Oriented Programming \(OOP\). We normally use it to initialize all the variables.

```python
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)
```

**Output**

```text
2+3j
(5, 0, 10)
Traceback (most recent call last):
  File "<string>", line 27, in <module>
    print(num1.attr)
AttributeError: 'ComplexNumber' object has no attribute 'attr'
```

In the above example, we defined a new class to represent complex numbers. It has two functions, `__init__()` to initialize the variables \(defaults to zero\) and `get_data()` to display the number properly.

An interesting thing to note in the above step is that attributes of an object can be created on the fly. We created a new attribute attr for object num2 and read it as well. But this does not create that attribute for object num1.

### Deleting Attributes and Objects <a id="delete"></a>

Any attribute of an object can be deleted anytime, using the `del` statement. Try the following on the Python shell to see the output.

```python
>>> num1 = ComplexNumber(2,3)
>>> del num1.imag
>>> num1.get_data()
Traceback (most recent call last):
...
AttributeError: 'ComplexNumber' object has no attribute 'imag'

>>> del ComplexNumber.get_data
>>> num1.get_data()
Traceback (most recent call last):
...
AttributeError: 'ComplexNumber' object has no attribute 'get_data'
```

We can even delete the object itself, using the del statement.

```python
>>> c1 = ComplexNumber(1,3)
>>> del c1
>>> c1
Traceback (most recent call last):
...
NameError: name 'c1' is not defined
```

Actually, it is more complicated than that. When we do `c1 = ComplexNumber(1,3)`, a new instance object is created in memory and the name c1 binds with it.

On the command `del c1`, this binding is removed and the name c1 is deleted from the corresponding namespace. The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.

This automatic destruction of unreferenced objects in Python is also called garbage collection.![Deleting Object in Python](https://cdn.programiz.com/sites/tutorial2program/files/objectReference.jpg)Deleting objects in Python removes the name binding

