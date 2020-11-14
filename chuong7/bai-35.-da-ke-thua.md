---
description: Python Multiple Inheritance
---

# Bài 35. Đa kế thừa

* Ông cho cha kế thừa, cha cho con kế thừa thì con được kế thừa từ cả cha và ông.
* Một "người" có thể được kế thừa trực tiếp từ nhiều "người".

### Đa kế thừa trong Python \(Multiple Inheritance\) <a id="inheritance"></a>

Một lớp có thể được bắt nguồn từ nhiều hơn một lớp cơ sở \(lớp cha\) và như thế được gọi là đa kế thừa.

Trong đa kế thừa, các tính năng của tất cả các lớp cơ sở \(lớp cha\) được kế thừa vào lớp dẫn xuất \(lướp con\). Cú pháp của đa kế thừa tương tự như kế thừa đơn.

#### Ví dụ

```python
class Lopcha1:
    pass

class Lopcha2:
    pass

class Lopcondakethua(Lopcha1, Lopcha2):
    pass
```

Biểu đồ minh họa đa kế thừa từ 2 class.

![Multiple Inheritance in Python](https://cdn.programiz.com/sites/tutorial2program/files/MultipleInheritance.jpg)

### Kế thừa đa cấp trong Python \(Multilevel Inheritance\) <a id="multilevel"></a>

We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.

Ta có thể kế thừa từ một lớp dẫn xuất \(lớp con\) và như vậy được gọi là kế thừa đa cấp. Kế thừa đa cấp không giới hạn bao nhiêu cấp.

Trong kế thừa đa cấp, các tính năng của lớp cơ sở và lớp dẫn xuất được kế thừa vào lớp dẫn xuất mới.

Ví dụ

```python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

Ở ví dụ này, lớp Derived1 có nguồn gốc từ lớp Cơ sở và lớp Derived2 có nguồn gốc từ lớp Derived1.

![Multilevel Inheritance in Python](https://cdn.programiz.com/sites/tutorial2program/files/MultilevelInheritance.jpg)

### Thứ tự truy xuất phương thức \(Method Resolution Order\)

Mọi lớp trong Python đều có nguồn gốc từ lớp đối tượng. Nó là kiểu cơ sở nhất trong Python.

Vì vậy, về mặt kỹ thuật, tất cả các lớp khác, được tạo sẵn hoặc do người dùng định nghĩa, đều là các lớp dẫn xuất và tất cả các đối tượng là các thể hiện của lớp đối tượng.

```python
# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))
```

Trong kịch bản đa kế thừa, bất kỳ thuộc tính cần được truy xuất nào, đầu tiên sẽ được tìm kiếm trong lớp hiện tại. Nếu không tìm thấy, tìm kiếm tiếp tục vào lớp cha đầu tiên và từ trái qua phải.

Ở ví dụ đầu bài, lớp `Lopcondakethua` có thứ tự ưu tiên truy xuất như sau:   
\[`Lopcondakethua`, `Lopcha1`, `Lopcha2`, `object`\]. 

Để biết thứ tự truy xuất ta có thể dùng phương thức `__mro__` hoặc `mro()`. `__mro__` trả về một tuple còn `mro()` trả về một list

```python
class Lopcha1:
    pass

class Lopcha2:
    pass

class Lopcondakethua(Lopcha1, Lopcha2):
    pass

print(Lopcondakethua.__mro__)    
print(Lopcondakethua.mro())
```

Output:

```python
(<class '__main__.Lopcondakethua'>, 
<class '__main__.Lopcha1'>, 
<class '__main__.Lopcha2'>, 
<class 'object'>)

[<class '__main__.Lopcondakethua'>, 
<class '__main__.Lopcha1'>, 
<class '__main__.Lopcha2'>, 
<class 'object'>]
```

Dưới đây là một ví dụ thừa kế phức tạp và hiển thị trực quan của nó cùng với MRO.

![Multiple Inheritance Visualization](https://cdn.programiz.com/sites/tutorial2program/files/MRO.jpg)

```python
# Demonstration of MRO

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
```

**Output**

```python
[<class '__main__.M'>,
 <class '__main__.B'>,
 <class '__main__.A'>,
 <class '__main__.X'>,
 <class '__main__.Y'>,
 <class '__main__.Z'>,
 <class 'object'>]
```

