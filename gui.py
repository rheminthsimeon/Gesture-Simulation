import tkinter as tk
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.vid = cv2.VideoCapture(video_source)
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        self.hand_position = (320, 240)
        self.object_pos = [300, 200]
        self.object_grabbed = False
        self.gravity = 2

        self.delay = 15
        self.update_callback = None
        self.window.after(self.delay, self.update)

    def set_update_callback(self, callback):
        self.update_callback = callback

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.flip(frame, 1)

            if self.update_callback:
                frame, hand_pos, grab, objects = self.update_callback(frame)

                self.hand_position = hand_pos
                if grab:
                    self.object_grabbed = True
                    self.object_pos[0], self.object_pos[1] = hand_pos
                else:
                    self.object_grabbed = False

            if not self.object_grabbed:
                self.object_pos[1] += self.gravity
                if self.object_pos[1] > 470:
                    self.object_pos[1] = 470

            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

            # Draw virtual object
            x, y = self.object_pos
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='red')

            # Draw virtual robot arm
            hx, hy = self.hand_position
            self.canvas.create_oval(hx-15, hy-15, hx+15, hy+15, outline='green', width=3)

            self.photo = imgtk

        self.window.after(self.delay, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()