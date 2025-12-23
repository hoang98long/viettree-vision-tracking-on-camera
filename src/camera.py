import cv2

def open_camera(cfg):
    if cfg["type"] == "usb":
        cap = cv2.VideoCapture(int(cfg["source"]))
    elif cfg["type"] == "rtsp":
        cap = cv2.VideoCapture(cfg["source"])
    else:
        cap = cv2.VideoCapture(cfg["source"])

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cfg["width"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg["height"])

    if not cap.isOpened():
        raise RuntimeError("Cannot open camera")

    return cap
