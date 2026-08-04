from pathlib import Path
import json


def ensure_directory(path: Path):
    """
    Tạo thư mục nếu chưa tồn tại.
    """

    path.mkdir(
        parents=True,
        exist_ok=True
    )


def load_json(path: Path, default=None):
    """
    Đọc file JSON an toàn.
    """

    try:

        if not path.exists():
            return default

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return default



def save_json(path: Path, data):
    """
    Lưu dữ liệu JSON.
    """

    ensure_directory(
        path.parent
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def format_date(value: str):
    """
    Chuẩn hóa ngày GS1:
    YYMMDD -> YYYY-MM-DD
    """

    if not value or len(value) != 6:
        return value


    year = int(value[:2])

    month = value[2:4]

    day = value[4:6]


    year += 2000


    return f"{year:04d}-{month}-{day}"