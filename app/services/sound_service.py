from pathlib import Path

from PySide6.QtMultimedia import (
    QAudioOutput,
    QMediaPlayer
)

from app.core.constants import (
    SUCCESS_SOUND,
    ERROR_SOUND
)


class SoundService:
    """
    Phát âm thanh phản hồi khi quét.
    """

    def __init__(self):

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setAudioOutput(
            self.audio
        )


    def play_success(self):

        self._play(
            SUCCESS_SOUND
        )


    def play_error(self):

        self._play(
            ERROR_SOUND
        )


    def _play(self, file: Path):

        if not file.exists():
            return

        self.player.stop()

        self.player.setSource(
            file.as_uri()
        )

        self.player.play()