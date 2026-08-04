from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class BarcodeResult:
    """
    Kết quả cuối cùng của 1 barcode/QR
    """

    # Nội dung barcode
    text: str = ""

    # QR_CODE / DATAMATRIX / ...
    format: str = ""

    # 4 điểm của barcode trên ảnh gốc
    polygon: List[List[int]] = field(default_factory=list)

    # Đọc thành công hay không
    success: bool = False

    # Dữ liệu GS1 sau khi parse
    gs1: Dict = field(default_factory=dict)

    # Thời gian decode (ms)
    elapsed_ms: float = 0

    # Chất lượng (để dành)
    score: float = 0