from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QLabel,
    QPlainTextEdit
)


class ResultWidget(QWidget):

    """
    Hiển thị kết quả GS1 sau khi quét.
    """


    def __init__(self, parent=None):

        super().__init__(parent)

        self._build_ui()



    def _build_ui(self):


        layout = QVBoxLayout(
            self
        )



        infoBox = QGroupBox(
            "GS1 Information"
        )


        form = QFormLayout(
            infoBox
        )



        self.lblBarcodeType = QLabel("-")

        self.lblGTIN = QLabel("-")

        self.lblBatch = QLabel("-")

        self.lblSerial = QLabel("-")

        self.lblProduction = QLabel("-")

        self.lblExpire = QLabel("-")

        self.lblTime = QLabel("-")



        form.addRow(
            "Barcode Type",
            self.lblBarcodeType
        )


        form.addRow(
            "GTIN",
            self.lblGTIN
        )


        form.addRow(
            "Batch / Lot",
            self.lblBatch
        )


        form.addRow(
            "Serial",
            self.lblSerial
        )


        form.addRow(
            "Production Date",
            self.lblProduction
        )


        form.addRow(
            "Expiration Date",
            self.lblExpire
        )


        form.addRow(
            "Scan Time",
            self.lblTime
        )



        layout.addWidget(
            infoBox
        )





        rawBox = QGroupBox(
            "Raw Data"
        )


        rawLayout = QVBoxLayout(
            rawBox
        )


        self.txtRaw = QPlainTextEdit()

        self.txtRaw.setReadOnly(
            True
        )


        rawLayout.addWidget(
            self.txtRaw
        )



        layout.addWidget(
            rawBox
        )


        layout.addStretch()




    def set_result(
        self,
        data: dict
    ):


        self.lblBarcodeType.setText(
            data.get(
                "barcode_type",
                "-"
            )
        )


        self.lblGTIN.setText(
            data.get(
                "gtin",
                "-"
            )
        )


        self.lblBatch.setText(
            data.get(
                "batch",
                "-"
            )
        )


        self.lblSerial.setText(
            data.get(
                "serial",
                "-"
            )
        )


        self.lblProduction.setText(
            data.get(
                "production",
                "-"
            )
        )


        self.lblExpire.setText(
            data.get(
                "expire",
                "-"
            )
        )


        self.lblTime.setText(
            data.get(
                "scan_time",
                "-"
            )
        )


        self.txtRaw.setPlainText(
            data.get(
                "raw",
                ""
            )
        )




    def clear(self):


        self.set_result(
            {}
        )