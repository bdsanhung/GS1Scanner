
from PySide6.QtGui import (
    QPixmap,
    QPainter,
    QPen,
    QPolygonF
)

from PySide6.QtCore import (
    Qt,
    QPointF
)
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class CameraWidget(QWidget):

    """
    Widget hiển thị camera realtime.
    """


    def __init__(
        self,
        parent=None
        
    ):

        super().__init__(parent)
        self.current_pixmap = None
        self._build_ui()
        self.scan_ok = False
        self.barcode_results = []
        self.original_width = 1920
        self.original_height = 1080
        self.display_offset_x = 0
        self.display_offset_y = 0


    # def paintEvent(self, event):

    #     super().paintEvent(event)


    #     if self.current_pixmap is None:
    #         return



    #     displayed = self.imageLabel.pixmap()


    #     if displayed is None:
    #         return



    #     painter = QPainter(
    #         self.imageLabel
    #     )



    #     pen = QPen(
    #         Qt.red,
    #         3
    #     )

    #     painter.setPen(
    #         pen
    #     )



    #     w = int(
    #         displayed.width() * 0.6
    #     )


    #     h = int(
    #         displayed.height() * 0.6
    #     )


    #     x = int(
    #         (displayed.width() - w) / 2
    #     )


    #     y = int(
    #         (displayed.height() - h) / 2
    #     )



    #     painter.drawRect(
    #         x,
    #         y,
    #         w,
    #         h
    #     )


    #     painter.end()


    def set_barcode_results(self, results):

        self.barcode_results = results

        if self.current_pixmap:
            self.set_pixmap(
                self.current_pixmap
            )

        self.barcode_results = results

        self.update()
    def set_scan_status(
        self,
        success: bool
    ):

        self.scan_ok = success

        self.update()
    def _build_ui(self):


        layout = QVBoxLayout(
            self
        )


        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )



        self.imageLabel = QLabel(
            "Camera Preview"
        )


        self.imageLabel.setAlignment(
            Qt.AlignCenter
        )


        self.imageLabel.setFixedSize(
                800,
                600
            )


        self.imageLabel.setStyleSheet(
            """
            QLabel {
                background-color: #111111;
                color: #eeeeee;
                border: 1px solid #555555;
                font-size: 18px;
            }
            """
        )


        layout.addWidget(
            self.imageLabel
        )




    def set_pixmap(self, pixmap):

        if pixmap.isNull():
            return


        self.original_width = pixmap.width()
        self.original_height = pixmap.height()


        scaled = pixmap.scaled(

            self.imageLabel.size(),

            Qt.KeepAspectRatio,

            Qt.SmoothTransformation

        )
        self.display_offset_x = (
            self.imageLabel.width()
            -
            scaled.width()
        ) // 2


        self.display_offset_y = (
            self.imageLabel.height()
            -
            scaled.height()
        ) // 2

        painter = QPainter(
            scaled
        )


        try:

            pen = QPen(
                Qt.green,
                4
            )

            painter.setPen(
                pen
            )
            # ROI màu đỏ
            

            roi_pen = QPen(
                Qt.red,
                3
            )

            painter.setPen(
                roi_pen
            )
            

            roi_w = int(
                scaled.width() * 0.6
            )


            roi_h = int(
                scaled.height() * 0.6
            )


            roi_x = (
                scaled.width()
                -
                roi_w
            ) // 2 + self.display_offset_x


            roi_y = (
                scaled.height()
                -
                roi_h
            ) // 2 + self.display_offset_y


            painter.drawRect(
                roi_x,
                roi_y,
                roi_w,
                roi_h
            )

            scale_x = (
                scaled.width()
                /
                self.original_width
            )


            scale_y = (
                scaled.height()
                /
                self.original_height
            )

            qr_pen = QPen(
                Qt.green,
                4
            )

            painter.setPen(
                qr_pen
            )
            for item in self.barcode_results:


                if item.position is None:
                    continue


                pos = item.position


                points = [

                    pos.top_left,

                    pos.top_right,

                    pos.bottom_right,

                    pos.bottom_left

                ]


                polygon = QPolygonF()


                for p in points:

                    polygon.append(

                        QPointF(

                            p.x * scale_x
                            +
                            self.display_offset_x,


                            p.y * scale_y
                            +
                            self.display_offset_y

                        )

                    )


                painter.drawPolygon(
                    polygon
                )


        finally:

            painter.end()



        self.imageLabel.setPixmap(
            scaled
        )



    def clear(self):

        self.imageLabel.clear()


        self.imageLabel.setText(
            "Camera Preview"
        )