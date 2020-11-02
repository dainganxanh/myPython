# Cài Sublime Text để code Python
## Share key SublimeTex
```
Key Sublime Text 3.2.1 Build 3207

—– BEGIN LICENSE —–
Member J2TeaM
Single User License
EA7E-1011316
D7DA350E 1B8B0760 972F8B60 F3E64036
B9B4E234 F356F38F 0AD1E3B7 0E9C5FAD
FA0A2ABE 25F65BD8 D51458E5 3923CE80
87428428 79079A01 AA69F319 A1AF29A4
A684C2DC 0B1583D4 19CBD290 217618CD
5653E0A0 BACE3948 BB2EE45E 422D2C87
DD9AF44B 99C49590 D2DBDEE1 75860FD2
8C8BB2AD B2ECE5A4 EFC08AF2 25A9B864
—— END LICENSE ——
```

## Cài đặt để run Python
Mở sublimeText chọn từ menu:

Tools -> Build System -> New Build System...

Gõ đoạn code sau:
```
{
    "cmd": ["c:/Python/python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "env": {"PYTHONIOENCODING": "utf-8"}, 
}
```
Lưu ý: 

- Đường dẫn đến file python.exe phải chính xác theo máy cụ thể (lúc cài đặt Python)
- Dòng env": {"PYTHONIOENCODING": "utf-8"} là để giúp Sublime Text có thể run Python với Unicode.

Bước tiếp theo là lưu file với tên tùy chọn theo cấu trúc: <Tên tùy chọn>.sublime-build

Ví dụ: Python3x.sublime-build

Lúc này ta sẽ thấy trong list các trình biên dịch được liệt kê sẽ có thêm Python3x. Check chọn để build code Python.

All done!
