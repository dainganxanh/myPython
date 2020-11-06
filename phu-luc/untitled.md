# Cài Sublime Text để code Python

### Cài đặt để run Python

Mở SublimeText chọn từ menu:

`Tools -> Build System -> New Build System...`

Gõ đoạn code sau:

```text
{
    "cmd": ["c:/Python/python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "env": {"PYTHONIOENCODING": "utf-8"}, 
}
```

_**Lưu ý:**_

* Đường dẫn đến file python.exe phải chính xác theo máy cụ thể \(lúc cài đặt Python\)
* Dòng `env": {"PYTHONIOENCODING": "utf-8"}` là để giúp Sublime Text có thể run Python với Unicode.

Bước tiếp theo là lưu file với tên tùy chọn theo cấu trúc: `<Tên tùy chọn>.sublime-build`

Ví dụ: `Python 3x.sublime-build`

Lúc này ta sẽ thấy trong list các trình biên dịch được liệt kê sẽ có thêm `Python 3x`. Check chọn để build code Python.

![&#x1EA2;nh ch&#x1EE5;p m&#xE0;n h&#xEC;nh](../.gitbook/assets/image%20%281%29.png)

