import cv2
import numpy as np


class DetectorService:
    """
    Chỉ phát hiện vị trí QR.
    Không decode.
    """

    def __init__(self):

        self.detector = cv2.QRCodeDetector()

        self.roi_ratio = 0.6

    def detect(self, frame):

        if frame is None:
            return []

        h, w = frame.shape[:2]

        roi_w = int(w * self.roi_ratio)
        roi_h = int(h * self.roi_ratio)

        roi_x = (w - roi_w) // 2
        roi_y = (h - roi_h) // 2

        roi = frame[
            roi_y:roi_y + roi_h,
            roi_x:roi_x + roi_w
        ]

        try:

            ok, points = self.detector.detectMulti(roi)

            if not ok or points is None:
                return []

            polygons = []

            for p in points:

                p = np.array(p, dtype=np.int32)

                # Chuyển từ tọa độ ROI sang tọa độ ảnh gốc
                p[:, 0] += roi_x
                p[:, 1] += roi_y

                polygons.append(p)

            return polygons

        except Exception:

            return []

    def get_roi_rect(self, frame):

        h, w = frame.shape[:2]

        roi_w = int(w * self.roi_ratio)
        roi_h = int(h * self.roi_ratio)

        roi_x = (w - roi_w) // 2
        roi_y = (h - roi_h) // 2

        return (
            roi_x,
            roi_y,
            roi_w,
            roi_h
        )