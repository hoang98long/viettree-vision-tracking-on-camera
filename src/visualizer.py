import cv2

def draw(frame, tracks, counts, line_y):
    h, w = frame.shape[:2]
    cv2.line(frame, (0,line_y), (w,line_y), (0,0,255), 2)

    for t in tracks:
        x1,y1,x2,y2 = map(int, t.bbox)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame,f"{t.cls}-{t.id}",
                    (x1,y1-5),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)

    y = 30
    for k,v in counts.items():
        cv2.putText(frame,f"{k}: {v}",
                    (20,y),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
        y += 30
