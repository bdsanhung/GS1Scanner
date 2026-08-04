# GS1 Scanner

Ứng dụng quét và phân tích mã GS1 sử dụng Python + PySide6.

## Tính năng

- Hiển thị camera realtime.
- Quét barcode/2D code.
- Phân tích GS1 Application Identifier:
  - (01) GTIN
  - (10) Batch/Lot
  - (11) Production Date
  - (17) Expiration Date
  - (21) Serial Number
- Lưu lịch sử quét.
- Phát âm thanh OK/NG.
- Kiến trúc mở rộng:
  - Camera Engine
  - Decoder Engine
  - GS1 Parser
  - UI Layer

## Yêu cầu

- Windows 10/11
- Python 3.11+

## Cài đặt

Tạo môi trường ảo:

```powershell
python -m venv .venv

.\.venv\Scripts\activate

pip install -r requirements.txt

.\build.ps1