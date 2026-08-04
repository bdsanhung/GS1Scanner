from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict


@dataclass
class GS1Data:
    """
    Model dữ liệu GS1 chuẩn.

    Dùng chung cho:
    - Scanner
    - Parser
    - History
    - Database
    - API/MES
    """

    raw: str = ""

    barcode_type: str = ""

    gtin: str = ""

    batch: str = ""

    serial: str = ""

    production: str = ""

    expire: str = ""

    scan_time: str = ""


    def __post_init__(self):

        if not self.scan_time:

            self.scan_time = (
                datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )



    def to_dict(self) -> Dict:

        return asdict(
            self
        )



    @staticmethod
    def from_dict(
        data: Dict
    ):

        return GS1Data(

            raw=data.get(
                "raw",
                ""
            ),

            barcode_type=data.get(
                "barcode_type",
                ""
            ),

            gtin=data.get(
                "gtin",
                ""
            ),

            batch=data.get(
                "batch",
                ""
            ),

            serial=data.get(
                "serial",
                ""
            ),

            production=data.get(
                "production",
                ""
            ),

            expire=data.get(
                "expire",
                ""
            ),

            scan_time=data.get(
                "scan_time",
                ""
            )
        )