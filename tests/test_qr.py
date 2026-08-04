import cv2
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)


while True:

    ok, frame = cap.read()

    if not ok:
        continue


    result = decode(frame)


    for item in result:

        print(
            item.type,
            item.data.decode("utf-8")
        )


    cv2.imshow(
        "test",
        frame
    )


    if cv2.waitKey(1)==27:
        break


cap.release()
cv2.destroyAllWindows()