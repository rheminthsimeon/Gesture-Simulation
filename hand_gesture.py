import cv2 
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def detect_hand(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    landmarks = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((id, cx, cy))
    return landmarks

def is_pinch(landmarks, threshold=40):
    if len(landmarks) >= 9:
        _, x1, y1 = landmarks[4]  # Thumb tip
        _, x2, y2 = landmarks[8]  # Index tip
        dist = np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2]))
        return dist < threshold
    return False
