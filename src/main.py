import cv2, json
from camera import open_camera
from detector import YOLODetector
from tracker import SimpleTracker
from counter import LineCounter
from visualizer import draw
from utils import load_yaml, FPS

# Load config
sys_cfg = load_yaml("config/system.yaml")
cam_cfg = load_yaml("config/camera.yaml")
model_cfg = load_yaml("config/model.yaml")
counter_cfg = load_yaml("config/counter.yaml")

class_map = {v:k for k,v in counter_cfg["classes"].items()}

# Init
cap = open_camera(cam_cfg)
detector = YOLODetector(model_cfg["model_path"], model_cfg["conf_threshold"])
tracker = SimpleTracker()
counter = LineCounter(counter_cfg["line_y"], class_map)
fps = FPS()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    boxes, classes = detector.detect(frame)

    detections = []
    for box, cls_id in zip(boxes, classes):
        if cls_id in class_map:
            detections.append((box, class_map[cls_id]))

    tracks = tracker.update(detections)
    counter.update(tracks)

    draw(frame, tracks, counter.counts, counter_cfg["line_y"])
    fps.update()

    if sys_cfg["show_window"]:
        cv2.imshow("Vision Counter", frame)
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()

with open("output/counts.json","w") as f:
    json.dump(counter.counts,f,indent=2)
