import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtGui import QImage, QPixmap


class CameraWorker(QObject):

    frameReady = Signal(QPixmap)
    frameCaptured = Signal(object)

    error = Signal(str)
    finished = Signal()


    def __init__(self, camera_index=0):

        super().__init__()

        self.camera_index = camera_index

        self.running = False

        self.cap = None



    def run(self):

        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():

            self.cap = cv2.VideoCapture(
                self.camera_index,
                cv2.CAP_DSHOW
            )


        if not self.cap.isOpened():

            self.error.emit(
                "Không mở được camera"
            )

            self.finished.emit()

            return



        self.running = True



        while self.running:


            ok, frame = self.cap.read()


            if not ok:

                continue



            # gửi frame gốc cho scanner

            self.frameCaptured.emit(
                frame.copy()
            )



            # convert hiển thị

            rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )


            h, w, ch = rgb.shape


            image = QImage(
                rgb.data,
                w,
                h,
                ch * w,
                QImage.Format_RGB888
            )


            pixmap = QPixmap.fromImage(
                image
            )


            self.frameReady.emit(
                pixmap
            )



        if self.cap:

            self.cap.release()


        self.finished.emit()



    def stop(self):

        self.running = False





class CameraService(QObject):

    frameReady = Signal(QPixmap)

    frameCaptured = Signal(object)

    error = Signal(str)



    def __init__(self):

        super().__init__()

        self.thread = None

        self.worker = None




    @staticmethod
    def get_camera_list(max_devices=5):

        cameras = []

        for i in range(max_devices):

            cap = cv2.VideoCapture(i)

            if cap.isOpened():

                ret, _ = cap.read()

                if ret:
                    cameras.append(f"Camera {i}")

            cap.release()

        return cameras



    def start(self, index=0):

        self.stop()



        self.thread = QThread()


        self.worker = CameraWorker(
            index
        )


        self.worker.moveToThread(
            self.thread
        )



        self.thread.started.connect(
            self.worker.run
        )



        self.worker.frameReady.connect(
            self.frameReady.emit
        )


        self.worker.frameCaptured.connect(
            self.frameCaptured.emit
        )


        self.worker.error.connect(
            self.error.emit
        )



        self.worker.finished.connect(
            self.thread.quit
        )


        self.worker.finished.connect(
            self.worker.deleteLater
        )


        self.thread.finished.connect(
            self.thread.deleteLater
        )



        self.thread.start()





    def stop(self):

        if self.worker:

            self.worker.stop()



        if self.thread:

            self.thread.quit()

            self.thread.wait()



        self.worker = None

        self.thread = None