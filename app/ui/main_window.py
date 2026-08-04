from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
    QStatusBar,
    QVBoxLayout,
    QWidget,
    QLabel
)


from app.ui.widgets.camera_widget import CameraWidget
from app.ui.widgets.result_widget import ResultWidget
from app.ui.widgets.toolbar_widget import ToolbarWidget


from app.services.camera_service import CameraService
from app.services.scanner_service import ScannerService
from app.services.gs1_parser import GS1Parser
from app.services.history_service import HistoryService
from app.services.sound_service import SoundService


from app.models.gs1 import GS1Data



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "GS1 Scanner"
        )

        self.resize(
            1400,
            850
        )


        self.cameraService = CameraService()

        self.scannerService = ScannerService()

        self.parser = GS1Parser()

        self.history = HistoryService()

        self.sound = SoundService()


        self._create_ui()

        self._connect_signal()

        self._load_style()


        # Tự động mở camera mặc định
        self.start_camera()
        self.scan_enable()



    def _create_ui(self):


        central = QWidget()

        self.setCentralWidget(
            central
        )


        layout = QVBoxLayout(
            central
        )


        self.toolbar = ToolbarWidget()


        layout.addWidget(
            self.toolbar
        )



        splitter = QSplitter(
            Qt.Horizontal
        )



        self.cameraWidget = CameraWidget()

        self.resultWidget = ResultWidget()



        splitter.addWidget(
            self.cameraWidget
        )


        splitter.addWidget(
            self.resultWidget
        )



        splitter.setStretchFactor(
            0,
            3
        )


        splitter.setStretchFactor(
            1,
            2
        )



        layout.addWidget(
            splitter
        )



        self.statusLabel = QLabel(
            "Ready"
        )


        status = QStatusBar()

        self.setStatusBar(
            status
        )


        status.addWidget(
            self.statusLabel
        )
        cameras = self.cameraService.get_camera_list()

        self.toolbar.set_camera_list(
            cameras
        )





    def _connect_signal(self):


        # Toolbar

        self.toolbar.startClicked.connect(
            self.start_camera
        )


        self.toolbar.stopClicked.connect(
            self.stop_camera
        )


        self.toolbar.scanClicked.connect(
            self.scan_enable
        )



        # Camera


        self.cameraService.frameReady.connect(
            self.cameraWidget.set_pixmap
        )


        self.cameraService.frameCaptured.connect(
            self.scannerService.set_frame
        )



        # Scanner


        self.scannerService.resultReady.connect(
            self.on_scan_result
        )


        self.scannerService.resultReady.connect(
            self.cameraWidget.set_barcode_results
        )
        self.scannerService.scanFailed.connect(
            lambda:
                self.cameraWidget.set_scan_status(False)
        )



    def start_camera(self):

        index = self.toolbar.current_camera()


        if index < 0:
            index = 0


        self.cameraService.start(
            index
        )


        self.statusLabel.setText(
            "Camera running"
        )





    def stop_camera(self):


        self.cameraService.stop()


        self.statusLabel.setText(
            "Camera stopped"
        )





    def scan_enable(self):


        self.scannerService.start()


        self.statusLabel.setText(
            "Scanning..."
        )





    def process_scan(
        self,
        results
    ):


        if not results:

            return



        item = results[0]



        parsed = self.parser.parse(
            item.text
        )



        data = GS1Data(

            raw=item.text,

            barcode_type=item.format,

            gtin=parsed["gtin"],

            batch=parsed["batch"],

            serial=parsed["serial"],

            production=parsed["production"],

            expire=parsed["expire"]

        )



        self.resultWidget.set_result(
            data.to_dict()
        )



        self.history.add(
            data.to_dict()
        )



        self.sound.play_success()



        self.statusLabel.setText(
            "Scan OK"
        )



    def _load_style(self):

        try:

            with open(
                "app/styles/theme.qss",
                "r",
                encoding="utf-8"
            ) as file:


                self.setStyleSheet(
                    file.read()
                )


        except Exception:

            pass




    def closeEvent(
        self,
        event
    ):


        self.scannerService.stop()

        self.cameraService.stop()


        event.accept()
    def on_scan_result(self, results):

        if not results:
            return


        for item in results:

            print(
                "GS1:",
                item.text,
                "FORMAT:",
                item.format
            )

        self.cameraWidget.update()
        # cập nhật khung QR xanh
        self.cameraWidget.set_barcode_results(
            results
        )