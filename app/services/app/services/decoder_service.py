import time
import cv2
import zxingcpp
import numpy as np

from app.models.barcode_result import BarcodeResult


class DecoderService:
    """
    Chỉ decode barcode.
    Không detect.
    """

    def decode(self, frame, polygons):

        results = []

        if frame is None:
            return results

        for polygon in polygons:

            polygon = np.array(
                polygon,
                dtype=np.int32
            )

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

                results.append(
                    BarcodeResult(
                        polygon=polygon.tolist(),
                        success=False
                    )
                )

                continue

            start = time.perf_counter()

            decoded = None

            images = [

                crop,

                cv2.cvtColor(
                    crop,
                    cv2.COLOR_BGR2GRAY
                )

            ]

            for img in images:

                try:

                    r = zxingcpp.read_barcodes(img)

                    if len(r) > 0:

                        decoded = r[0]

                        break

                except Exception:
                    pass

            elapsed = (
                time.perf_counter() - start
            ) * 1000

            if decoded is None:

                results.append(

                    BarcodeResult(

                        polygon=polygon.tolist(),

                        success=False,

                        elapsed_ms=elapsed

                    )

                )

            else:

                results.append(

                    BarcodeResult(

                        text=decoded.text,

                        format=str(decoded.format),

                        polygon=polygon.tolist(),

                        success=True,

                        elapsed_ms=elapsed

                    )

                )

        return results