# Thự Động Hóa Tra cứu Phạt Nguội

Đây là một script Python sử dụng **Selenium** và **Tesseract OCR** để tự động tra cứu thông tin **phạt nguội phương tiện giao thông** trên website Cục Cảnh Sát Giao Thông Việt Nam. Chương trình sẽ tự động chạy vào **6h sáng** và **12h trưa** mỗi ngày.

---

## Tính năng chính

- Tự động nhập biển số xe và loại phương tiện.
- Chụp ảnh mã captcha và nhận diện bằng OCR (Tesseract).
- Tự động gửi yêu cầu tra cứu kết quả vi phạm.
- Hẹn giờ chạy vào 06:00 và 12:00 hàng ngày bằng thư viện `schedule`.

---

## Yêu cầu hệ thống

- Python
- Google Chrome
- ChromeDriver (cùng phiên bản với Chrome)
- Tesseract OCR

---

## Cài đặt

### 1. Cài Python và pip

Tải Python từ: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Cài Tesseract OCR

- Tải Tesseract tại: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
-   Cài đặt và nhớ đường dẫn, ví dụ:

> Sau đó, mở file `.py` và chỉnh dòng:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
 thành đúng đường dẫn Tesseract của bạn.
### 3.  Cài ChromeDriver
-   Tải ChromeDriver tại: https://chromedriver.chromium.org/downloads
-   Giải nén và đặt cùng thư mục với file .py, hoặc cấu hình vào PATH.
### 4. Cài thư viện cần thiết
- selenium==4.32.0
- pillow==11.2.1
- pytesseract==0.3.13
- schedule==1.2.2
##  Cách chạy chương trình
Chạy file Python bằng lệnh:

```
python phatnguoiphatnguoi.py
```
Màn hình sẽ hiển thị: Đang chạy...
Chương trình sẽ tự động chạy mỗi ngày lúc 06:00 và 12:00.
##  Cấu trúc thư mục
```
📁 PHATNGUOI/
├── phatnguoi.py
├── requirements.txt
└── README.md
```

