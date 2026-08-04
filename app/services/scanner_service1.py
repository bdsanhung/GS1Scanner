from PySide6.QtCore import QObject, QTimer, Signal

from app.services.decoder_engine import (
    DecoderEngine,
    ZXingDecoder
)


class ScannerService(QObject):

    resultReady = Signal(list)

    scanFailed = Signal()

    error = Signal(str)

    def __init__(
        self,
        decoder: DecoderEngine = None
    ):

        super().__init__()

        self.decoder = decoder if decoder else ZXingDecoder()

        self.current_frame = None

        self.running = False

        self.last_values = set()

        self.timer = QTimer()

        self.timer.timeout.connect(
            self._scan
        )

    def set_frame(self, frame):

        self.current_frame = frame

    def start(self):

        if self.running:
            return

        self.running = True

        self.timer.start(100)

    def stop(self):

        self.running = False

        self.timer.stop()

        self.current_frame = None

        self.last_values.clear()

    def _scan(self):

        if self.current_frame is None:
            return

        try:

            results = self.decoder.decode(
                self.current_frame
            )

            if len(results) == 0:

                self.scanFailed.emit()

                return

            current = set()

            for item in results:

                if item.success:

                    current.add(item.text)

            if current == self.last_values:

                self.resultReady.emit(results)

                return

            self.last_values = current

            self.resultReady.emit(results)

        except Exception as ex:

            self.error.emit(str(ex))