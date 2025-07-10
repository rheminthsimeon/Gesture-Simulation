from gui import App
from object_tracker import detect_objects
from hand_gesture import detect_hand, is_pinch
import tkinter as tk

def process_frame(frame):
    hand_landmarks = detect_hand(frame)
    objects, _ = detect_objects(frame)
    pinch = is_pinch(hand_landmarks)

    hand_pos = (0, 0)
    if hand_landmarks:
        _, hand_x, hand_y = hand_landmarks[8]  # index tip
        hand_pos = (hand_x, hand_y)

    return frame, hand_pos, pinch, objects

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, "Gesture Simulation")
    app.set_update_callback(process_frame)
    root.mainloop()
