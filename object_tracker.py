import cv2
import numpy as np

def detect_objects(frame, lower_color=(30, 150, 50), upper_color=(85, 255, 255)):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    objects = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            cx, cy = x + w//2, y + h//2
            objects.append({'position': (cx, cy), 'rect': (x, y, w, h)})
    return objects, mask
