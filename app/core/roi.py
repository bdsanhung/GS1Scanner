ROI_WIDTH_RATIO = 0.6

ROI_HEIGHT_RATIO = 0.6



def get_roi(frame):

    if frame is None:
        return None


    h, w = frame.shape[:2]


    roi_w = int(
        w * ROI_WIDTH_RATIO
    )


    roi_h = int(
        h * ROI_HEIGHT_RATIO
    )


    x = int(
        (w - roi_w) / 2
    )


    y = int(
        (h - roi_h) / 2
    )


    return frame[
        y:y+roi_h,
        x:x+roi_w
    ]