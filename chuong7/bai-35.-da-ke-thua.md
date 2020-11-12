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

class Lopcondakethua(Base1, Base2):
    pass
```

Biểu đồ minh họa đa kế thừa từ 2 class.

![Multiple Inheritance in Python](https://cdn.programiz.com/sites/tutorial2program/files/MultipleInheritance.jpg)

### Python Multilevel Inheritance <a id="multilevel"></a>

We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.

In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.

An example with corresponding visualization is given below.

```python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

Here, the Derived1 class is derived from the Base class, and the Derived2 class is derived from the Derived1 class.![Multilevel Inheritance in Python](https://cdn.programiz.com/sites/tutorial2program/files/MultilevelInheritance.jpg)Multilevel Inheritance in Python

### Method Resolution Order in Python <a id="resolution"></a>

Every class in Python is derived from the `object` class. It is the most base type in Python.

So technically, all other classes, either built-in or user-defined, are derived classes and all objects are instances of the `object` class.

```python
# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))
```

In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.

So, in the above example of `MultiDerived` class the search order is \[`MultiDerived`, `Base1`, `Base2`, `object`\]. This order is also called linearization of `MultiDerived` class and the set of rules used to find this order is called **Method Resolution Order \(MRO\)**.

MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents. In case of multiple parents, the order is the same as tuples of base classes.

MRO of a class can be viewed as the `__mro__` attribute or the `mro()` method. The former returns a tuple while the latter returns a list.

```python
>>> MultiDerived.__mro__
(<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>)

>>> MultiDerived.mro()
[<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>]
```

Here is a little more complex multiple inheritance example and its visualization along with the MRO.![Multiple Inheritance Visualization](https://cdn.programiz.com/sites/tutorial2program/files/MRO.jpg)Visualizing Multiple Inheritance in Python

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

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]

print(M.mro())
```

**Output**

```python
[<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
```

To know the actual algorithm on how MRO is calculated, visit [Discussion on MRO](http://www.python.org/download/releases/2.3/mro/).

