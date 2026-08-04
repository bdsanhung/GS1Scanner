import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict


from app.core.constants import (
    MAX_HISTORY_RECORDS
)

from app.core.config import DATA_DIR



HISTORY_FILE = DATA_DIR / "history.json"



class HistoryService:
    """
    Quản lý lịch sử quét GS1.

    Chức năng:
    - Lưu lịch sử
    - Đọc lịch sử
    - Xóa lịch sử
    - Tự phục hồi file lỗi
    """



    def __init__(self):

        DATA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        self._initialize()



    def _initialize(self):

        if not HISTORY_FILE.exists():

            self._save([])



    def load(self) -> List[Dict]:

        try:

            with open(
                HISTORY_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(
                    file
                )


                if isinstance(
                    data,
                    list
                ):

                    return data



        except Exception:

            pass



        return []



    def add(
        self,
        data: Dict
    ):

        history = self.load()



        record = {

            "scan_time":
                datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            **data

        }



        history.insert(
            0,
            record
        )



        if len(history) > MAX_HISTORY_RECORDS:

            history = history[
                :MAX_HISTORY_RECORDS
            ]



        self._save(
            history
        )



    def clear(self):

        self._save([])



    def delete_last(self):

        history = self.load()


        if history:

            history.pop(0)


        self._save(
            history
        )



    def _save(
        self,
        data
    ):

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                data,

                file,

                ensure_ascii=False,

                indent=4

            )