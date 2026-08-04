import cv2
import numpy as np


class QRDetector:
    """
    Detect QR Code bằng OpenCV.
    Chỉ phát hiện vị trí, KHÔNG decode.
    """

    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def detect(self, frame):
        """
        Trả về danh sách polygon.

        [
            np.ndarray(
                [
                    [x1, y1],
                    [x2, y2],
                    [x3, y3],
                    [x4, y4]
                ]
            ),
            ...
        ]
        """

        if frame is None:
            return []

        try:

            ok, points = self.detector.detectMulti(frame)

            if not ok:
                return []

            if points is None:
                return []

            polygons = []

            for p in points:

                polygon = np.array(
                    p,
                    dtype=np.int32
                )

                polygons.append(polygon)

            return polygons

        except Exception:
            return []