from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QComboBox
)


class ToolbarWidget(QWidget):

    """
    Thanh điều khiển chính:

    - Chọn camera
    - Start camera
    - Stop camera
    - Bật/tắt scan
    """


    startClicked = Signal()

    stopClicked = Signal()

    scanClicked = Signal()

    settingsClicked = Signal()

    cameraChanged = Signal(int)



    def __init__(
        self,
        parent=None
    ):

        super().__init__(parent)

        self._build_ui()




    def _build_ui(self):


        layout = QHBoxLayout(
            self
        )


        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )



        self.cameraCombo = QComboBox()


        self.cameraCombo.setMinimumWidth(
            180
        )



        self.btnRefresh = QPushButton(
            "Refresh"
        )


        self.btnStart = QPushButton(
            "Start Camera"
        )


        self.btnStop = QPushButton(
            "Stop"
        )


        self.btnScan = QPushButton(
            "Scan"
        )


        self.btnSettings = QPushButton(
            "Settings"
        )



        layout.addWidget(
            self.cameraCombo
        )


        layout.addWidget(
            self.btnRefresh
        )


        layout.addWidget(
            self.btnStart
        )


        layout.addWidget(
            self.btnStop
        )


        layout.addWidget(
            self.btnScan
        )


        layout.addStretch()



        layout.addWidget(
            self.btnSettings
        )



        # Signals

        self.btnStart.clicked.connect(
            self.startClicked.emit
        )


        self.btnStop.clicked.connect(
            self.stopClicked.emit
        )


        self.btnScan.clicked.connect(
            self.scanClicked.emit
        )


        self.btnSettings.clicked.connect(
            self.settingsClicked.emit
        )


        self.cameraCombo.currentIndexChanged.connect(
            self.cameraChanged.emit
        )



    def set_camera_list(
        self,
        cameras
    ):


        self.cameraCombo.blockSignals(
            True
        )


        self.cameraCombo.clear()


        self.cameraCombo.addItems(
            cameras
        )


        self.cameraCombo.blockSignals(
            False
        )




    def current_camera(self):

        return (
            self.cameraCombo.currentIndex()
        )




    def clear_camera(self):

        self.cameraCombo.clear()