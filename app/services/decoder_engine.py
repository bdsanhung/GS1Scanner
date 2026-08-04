from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

import cv2
import numpy as np
import zxingcpp

from app.services.qr_detector import QRDetector


@dataclass
class DecodeResult:
    text: str
    format: str
    polygon: list
    success: bool


class DecoderEngine(ABC):

    @abstractmethod
    def decode(self, frame) -> List[DecodeResult]:
        pass


class ZXingDecoder(DecoderEngine):

    def __init__(self):
        self.detector = QRDetector()

    def decode(self, frame) -> List[DecodeResult]:

        if frame is None:
            return []

        polygons = self.detector.detect(frame)

        if len(polygons) == 0:
            return []

        output = []

        for polygon in polygons:

            polygon = np.array(polygon, dtype=np.int32)

            x = int(np.min(polygon[:, 0]))
            y = int(np.min(polygon[:, 1]))
            w = int(np.max(polygon[:, 0]) - x)
            h = int(np.max(polygon[:, 1]) - y)

            margin = 10

            x1 = max(0, x - margin)
            y1 = max(0, y - margin)

            x2 = min(frame.shape[1], x + w + margin)
            y2 = min(frame.shape[0], y + h + margin)

            crop = frame[y1:y2, x1:x2]

            if crop.size == 0:
                continue

            try:

                gray = cv2.cvtColor(
                    crop,
                    cv2.COLOR_BGR2GRAY
                )

                images = [
                    crop,
                    gray
                ]

                decoded = False

                for img in images:

                    results = zxingcpp.read_barcodes(img)

                    if len(results) > 0:

                        r = results[0]

                        output.append(

                            DecodeResult(

                                text=r.text,

                                format=str(r.format),

                                polygon=polygon.tolist(),

                                success=True

                            )

                        )

                        decoded = True

                        break

                if not decoded:

                    output.append(

                        DecodeResult(

                            text="",

                            format="",

                            polygon=polygon.tolist(),

                            success=False

                        )

                    )

            except Exception:

                output.append(

                    DecodeResult(

                        text="",

                        format="",

                        polygon=polygon.tolist(),

                        success=False

                    )

                )

        return output