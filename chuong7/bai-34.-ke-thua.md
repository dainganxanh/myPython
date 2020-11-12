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

Ở lớp Dagiac có các thuộc tính gồm số cạnh và một list lưu độ dài mỗi cạnh. Các phương thức nhapcanh\(\) và xemcanh\(\) để nhập độ dài cạnh và hiển thị các cạnh đã nhập.

Ta xây dựng class Tamgiac thừa kế từ lớp Dagiac. Theo đó lớp Tamgiac thừa kế tất cả các thuộc tính, phương thức từ lớp cha là class Dagiac. Vì vậy, dùng lớp Tamgiac không có phương thức nhapcanh\(\) và xemcanh\(\) nhưng ta vẫn có thể gọi và sử dụng trong chương trình.



### Method Overriding in Python <a id="method"></a>

Ở ví dụ trên ta thấy phương thức \_\_init\_\_\(\) được khai báo ở cả 2 class \(Dagiac và Tamgiac\). Trong trường hợp này phương thức \_\_init\_\_\(\) của lớp con sẽ ghi đề phương thức cùng tên của lớp cha. Nghĩa là phương thức instructor của Tamgiac ghi đè lên instructor của Dagiac.

Thông thường, việc ghi đè chỉ được dùng khi ta cần định nghĩa lại hoặc khai báo mới trong con so với lớp cha. Trường hợp không có gì khác thì gọi phương thức từ lớp cha để kế thừa \(dùng lệnh gọi `Dagiac.__init__()` trong `__init__()` của `Tamgiac`\).

Cách tốt hơn và thường được dùng hơn khi gọi kế thừa \_\_init\_\_ từ lớp cha người ta dùng hàm có sẵn super\(\). Thay vì gọi  `Dagiac.__init__(self, 3)` thì ta có thể gọi`super().__init__(3)` .

### Kiểm tra quan hệ 2 lớp

Hàm `isinstance()` và `issubclass()` được dùng để kiểm tra mối quan hệ của hai lớp và instance.

Hàm `issubclass(A, B)` trả về `True` nếu class A là lớp con của class B.

Hàm `isinstance(a,B)` trả về `True` nếu đối tượng a là một thể hiện \(instance\) của class B hoặc một class con của lớp B.

Ví dụ

```python
# True
print(isinstance(tg,Tamgiac))
# True
print(isinstance(tg,Dagiac))
# True
print(issubclass(Tamgiac,Dagiac))
# False
print(issubclass(Dagiac,Tamgiac))
```

