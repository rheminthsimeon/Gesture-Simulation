import cv2
import mediapipe as mp
import pygame
import numpy as np

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Pygame
pygame.init()
screen_width, screen_height = 960, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Palm Skeleton Simulation")
clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Ball
ball_radius = 30
ball_pos = [screen_width // 2, screen_height // 2]
grabbed = False

# Hand landmark connections for skeleton
HAND_CONNECTIONS = mp_hands.HAND_CONNECTIONS

# Helper: Convert OpenCV frame to Pygame surface
def cv_to_pygame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    return pygame.surfarray.make_surface(frame)

# Helper: Get palm center
def get_palm_center(landmarks):
    if len(landmarks) >= 18:
        pts = [landmarks[i] for i in [0, 5, 9, 13, 17]]
        center = np.mean(pts, axis=0).astype(int)
        return tuple(center)
    return None

# Helper: Pinch detection
def is_pinch(landmarks, threshold=40):
    if len(landmarks) >= 9:
        x1, y1 = landmarks[4]   # Thumb tip
        x2, y2 = landmarks[8]   # Index tip
        dist = np.linalg.norm([x1 - x2, y1 - y2])
        return dist < threshold
    return False

# Video capture
cap = cv2.VideoCapture(0)
cap.set(3, screen_width)
cap.set(4, screen_height)

# Main loop
running = True
while running:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    screen.fill(WHITE)
    surface = cv_to_pygame(frame)
    screen.blit(surface, (0, 0))

    landmarks = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))

            # Draw connections
            for conn in HAND_CONNECTIONS:
                start = landmarks[conn[0]]
                end = landmarks[conn[1]]
                pygame.draw.line(screen, GREEN, start, end, 2)

    palm_center = get_palm_center(landmarks)
    pinch = is_pinch(landmarks)

    # Ball interaction
    if palm_center:
        pygame.draw.circle(screen, YELLOW, palm_center, 20, 3)
        distance = np.linalg.norm(np.array(ball_pos) - np.array(palm_center))

        if pinch and distance < 50:
            grabbed = True
        elif not pinch:
            grabbed = False

        if grabbed:
            ball_pos = list(palm_center)

    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)

cap.release()
pygame.quit()
