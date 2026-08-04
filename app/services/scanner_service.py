from PySide6.QtCore import QObject, QTimer, Signal

from app.services.detector_service import DetectorService
from app.services.decoder_service import DecoderService


class ScannerService(QObject):

    # Trả về List[BarcodeResult]
    resultReady = Signal(list)

    scanFailed = Signal()

    error = Signal(str)

    def __init__(self):

        super().__init__()

        self.detector = DetectorService()

        self.decoder = DecoderService()

        self.current_frame = None

        self.running = False

        self.timer = QTimer()

        self.timer.timeout.connect(
            self._scan
        )

        self.last_results = []

    def set_frame(self, frame):

        self.current_frame = frame

    def start(self):

        if self.running:
            return

        self.running = True

        # Detect khoảng 15 FPS
        self.timer.start(66)

    def stop(self):

        self.running = False

        self.timer.stop()

        self.current_frame = None

        self.last_results.clear()

    def _scan(self):

        if self.current_frame is None:
            return

        try:

            polygons = self.detector.detect(
                self.current_frame
            )

            if len(polygons) == 0:

                self.last_results = []

                self.scanFailed.emit()

                return

            results = self.decoder.decode(
                self.current_frame,
                polygons
            )

            self.last_results = results

            self.resultReady.emit(
                results
            )

        except Exception as ex:

            self.error.emit(
                str(ex)
            )

    def get_roi_rect(self):

        if self.current_frame is None:
            return None

        return self.detector.get_roi_rect(
            self.current_frame
        )