---
description: Python Inheritance
---

# Bài 34. Kế thừa

### Kế thừa trong Python \(Inheritance\) <a id="what"></a>

Kế thừa là một tính năng mạnh mẽ trong lập trình hướng đối tượng. 

Kế thừa \(Inheritance\) cho phép một lớp \(class\) có thể kế thừa các thuộc tính và phương thức từ các lớp khác đã được định nghĩa. Lớp đã có gọi là lớp cha \(base class hoặc parent class\), lớp mới phát sinh gọi là lớp con \(child class hoặc derived class\). Lớp con kế thừa tất cả thành phần của lớp cha, có thể mở rộng các thành phần kế thừa và bổ sung thêm các thành phần mới.

#### Cú pháp khai báo <a id="syntax"></a>

```python
class LopCha:
  # Các thành phần trong lớp cha
class LopCon(LopCha):
  # Các thành phần trong lớp con
```

#### Ví dụ về kế thừa trong Python <a id="example"></a>

Xét ví dụ sau

```python
class Dagiac:
    def __init__(self, socanh):
        self.n = socanh
        self.canh = [0 for i in range(socanh)]

    def nhapcanh(self):
        self.canh = [float(input(f"Nhập cạnh {i+1}: ")) for i in range(self.n)]

    def xemcanh(self):
        for i in range(self.n):
            #print("Cạnh",i+1,"là",self.canh[i])
            print(f'Cạnh {i+1} là {self.canh[i]}')
            
class Tamgiac(Dagiac):
    def __init__(self):
        Dagiac.__init__(self,3)

    def dientichTG(self):
        a, b, c = self.canh
        s = (a + b + c) / 2
        dt = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f'Diện tích của tam giác là {dt:.2f}')            

tg = Tamgiac()

tg.nhapcanh()

tg.xemcanh()

tg.dientichTG()
```

```python
Nhập cạnh 1: 5
Nhập cạnh 2: 3
Nhập cạnh 3: 4

Cạnh 1 là 5.0
Cạnh 2 là 3.0
Cạnh 3 là 4.0
Diện tích của tam giác là 6.00
```

This class has data attributes to store the number of sides n and magnitude of each side as a list called sides.

The `inputSides()` method takes in the magnitude of each side and `dispSides()` displays these side lengths.

A triangle is a polygon with 3 sides. So, we can create a class called Triangle which inherits from Polygon. This makes all the attributes of Polygon class available to the Triangle class.

We don't need to define them again \(code reusability\). Triangle can be defined as follows.

```text
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
```

However, class `Triangle` has a new method `findArea()` to find and print the area of the triangle. Here is a sample run.

```text
>>> t = Triangle()

>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4

>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0

>>> t.findArea()
The area of the triangle is 6.00
```

We can see that even though we did not define methods like `inputSides()` or `dispSides()` for class `Triangle` separately, we were able to use them.

If an attribute is not found in the class itself, the search continues to the base class. This repeats recursively, if the base class is itself derived from other classes.

### Method Overriding in Python <a id="method"></a>

In the above example, notice that `__init__()` method was defined in both classes, Triangle as well Polygon. When this happens, the method in the derived class overrides that in the base class. This is to say, `__init__()` in Triangle gets preference over the `__init__` in Polygon.

Generally when overriding a base method, we tend to extend the definition rather than simply replace it. The same is being done by calling the method in base class from the one in derived class \(calling `Polygon.__init__()` from `__init__()` in `Triangle`\).

A better option would be to use the built-in function `super()`. So, `super().__init__(3)` is equivalent to `Polygon.__init__(self,3)` and is preferred. To learn more about the `super()` function in Python, visit [Python super\(\) function](http://rhettinger.wordpress.com/2011/05/26/super-considered-super/).

Two built-in functions `isinstance()` and `issubclass()` are used to check inheritances.

The function `isinstance()` returns `True` if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class `object`.

```text
>>> isinstance(t,Triangle)
True

>>> isinstance(t,Polygon)
True

>>> isinstance(t,int)
False

>>> isinstance(t,object)
True
```

Similarly, `issubclass()` is used to check for class inheritance.

```text
>>> issubclass(Polygon,Triangle)
False

>>> issubclass(Triangle,Polygon)
True

>>> issubclass(bool,int)
True
```

