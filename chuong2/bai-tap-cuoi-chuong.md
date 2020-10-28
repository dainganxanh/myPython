# Bài tập chương 2

## Bài tập 1

Cho trước 3 số nguyên x, y, z được từ file. Bạn hãy viết chương trình ghi kết quả ra file output.dat theo yêu cầu sau:

Nếu x là số chẵn, kiểm tra xem y có lớn hơn hoặc bằng 20 hay không. Nếu y &gt;= 20, ghi ra dòng chữ y is greater than or equal to 20; ngược lại, ghi ra dòng chữ y is less than 20.

Nếu x là số lẻ, kiểm tra xem z có lớn hơn hoặc bằng 30 hay không. Nếu z &gt;= 30, ghi ra dòng chữ z is greater than or equal to 30; ngược lại, ghi ra dòng chữ z is less than 30.

Ví dụ:

Với x = 20, y = 33, z = 15 thì kết quả là `y is greater than 20`  
Vì x % 2 == 0 và y &gt; 20  
Với x = 15, y = 23, z = 20  thì kết quả là `z is less than 30`  
Vì x % 2 != 0 và z &lt; 30

## Bài tập 2

Cho số nguyên age chỉ tuổi của vật nuôi được nhập từ file input.txt, bạn hãy hiển thị ra màn hình theo yêu cầu sau:

Nếu age &lt;= 0 thì hiển thị "This can hardly be true"  
Nếu age == 1 thì hiển thị "About 1 human year"  
Nếu age == 2 thì hiển thị "About 2 human years"  
Nếu age &gt; 2 thì hiển thị "Over 5 human years. 

Ví dụ nếu bạn nhập age = 3 thì hiển thị "Over 5 human years"  
Nếu bạn nhập age = 1 thì hiển thị "About 1 human year"

## Bài tập 3

Cho số nguyên dương n được nhập từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình tổng các số từ 1 tới n. Ví dụ nếu bạn nhập n = 5 thì màn hình sẽ hiển thị ra: 15

Giải thích: 1 + 2 + 3 + 4 + 5 = 15.

## Bài tập 4

Cho 2 số nguyên a và b được nhập từ file input.txt \(a cách b bởi một khoảng trắng\), hãy viết chương trình ghi các số lẻ từ a tới b ra file out.txt. Ví dụ nếu nội dung file input.txt là `3 9` thì nội dung file out.txt là: `24`

Giải thích: 3 + 5 + 7 + 9 = 24. Đầu vào luôn đảm bảo b &gt; a.

## Bài tập 5

Cho chuỗi s được nhập từ file input.txt, bạn hãy viết chương trình ghi các kí tự khác kí tự 'y' trong chuỗi s ra file out.txt. Ví dụ nội dung file input.txt là "`python`" thì nội dung file out.txt là:

`p  
t  
h  
o  
n`

## Bài tập 6

Cho số nguyên a được nhập từ bàn phím, bãn hãy viết chương trình hiển thị ra màn tích của a với các số từ 1 đến 5. Ví dụ nếu bạn nhập a = 10 thì màn hình sẽ hiển thị ra:

`10 * 1 = 10  
10 * 2 = 20  
10 * 3 = 30  
10 * 4 = 40  
10 * 5 = 50`

## Bài tập 7

Cho hai số nguyên a và b được nhâp từ file input.txt \(a cách b bởi một khoảng trắng\), hãy viết chương trình đếm số các số chẵn và số các số lẻ trong khoảng từ a tới b. Sau đó ghi vào file out.txt thông tin sau:

Ví dụ file input.txt là: `1 10`   
thì nội dung file out.txt là:

`Number of even numbers: 5  
Number of odd numbers: 5`

## Bài tập 8

Cho số nguyên n được nhập vào từ file in.txt, bạn hãy viết chương trình ghi ra file out.txt tổng của dãy số 1/2 + 2/3 + ... + n/n+1. Yêu cầu chỉ hiển thị 2 số thập phân sau phẩy.

Ví dụ:   
file in.txt là: `10` file out.txt sẽ là: `7.98`  
file in.txt là: `20` file out.txt sẽ là: `17.35`

