from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QSpinBox,
    QPushButton,
    QVBoxLayout,
    QLabel
)

from app.core.config import load_config, save_config


class SettingsDialog(QDialog):
    """
    Cửa sổ cấu hình ứng dụng.
    """

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle(
            "GS1 Scanner Settings"
        )

        self.config = load_config()

        self._build_ui()

        self._load_values()


    def _build_ui(self):

        layout = QVBoxLayout(self)

        form = QFormLayout()


        self.spinCamera = QSpinBox()
        self.spinCamera.setMinimum(0)
        self.spinCamera.setMaximum(20)


        self.spinInterval = QSpinBox()
        self.spinInterval.setMinimum(50)
        self.spinInterval.setMaximum(5000)


        form.addRow(
            QLabel("Camera Index"),
            self.spinCamera
        )

        form.addRow(
            QLabel("Scan Interval (ms)"),
            self.spinInterval
        )


        layout.addLayout(form)


        self.btnSave = QPushButton(
            "Save"
        )

        self.btnSave.clicked.connect(
            self.save
        )


        layout.addWidget(
            self.btnSave
        )


    def _load_values(self):

        camera = self.config.get(
            "camera",
            {}
        )

        scanner = self.config.get(
            "scanner",
            {}
        )


        self.spinCamera.setValue(
            camera.get(
                "default_index",
                0
            )
        )


        self.spinInterval.setValue(
            scanner.get(
                "scan_interval_ms",
                200
            )
        )


    def save(self):

        self.config["camera"][
            "default_index"
        ] = self.spinCamera.value()


        self.config["scanner"][
            "scan_interval_ms"
        ] = self.spinInterval.value()


        save_config(
            self.config
        )


        self.accept()