# Gesture-Controlled Object Manipulation

This repository provides two interactive simulations for gesture-based object manipulation using hand tracking:

- A **Tkinter GUI simulation** for controlling a virtual object via hand gestures (interlinked Python modules).
- A **standalone Pygame simulation** for palm skeleton and object interaction (located in the `standalone` folder).

## Features

- **Hand Gesture Detection:** Uses MediaPipe to detect hand landmarks via webcam.
- **Object Grabbing & Movement:** Grab and move a virtual object with a pinch gesture.
- **Gravity Simulation:** Objects fall when not grabbed (Tkinter version).
- **Visual Feedback:** Real-time drawing of hand positions, object location, and gesture states.

## Project Structure
├── main.py
├── gui.py
├── hand_gesture.py
├── object_tracker.py
└── standalone/
    └── pygame_sim.py

- `main.py`: Entry point for the Tkinter-based gesture simulation.
- `gui.py`: Handles GUI rendering and object/hand visualization.
- `hand_gesture.py`: Hand detection and pinch gesture logic.
- `object_tracker.py`: Color-based object detection utilities.
- `standalone/pygame_sim.py`: Standalone Pygame simulation (not linked to other modules).

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- Pillow (for Tkinter GUI)
- Tkinter (usually included with Python)
- Pygame (for standalone simulation)

Install dependencies with:
_pip install opencv-python mediapipe numpy pillow pygame_

## Usage

### Tkinter Gesture Simulation

1. Ensure your webcam is connected.
2. Run:
    
   _python main.py_
   

3. The GUI will open. Use your hand in front of the webcam:
   - **Pinch** (thumb and index finger tips close) to grab the red object.
   - Move your hand to move the object.
   - Release the pinch to drop the object (gravity will apply).

### Standalone Pygame Simulation

1. Navigate to the `standalone` folder:

   _cd standalone_

2. Run:
   _python pygame_sim.py_

3. Interact with the ball using pinch gestures. The palm skeleton and connections will be visualized.

## Notes

- The Tkinter simulation (`main.py` and related modules) is interdependent; do not run modules individually.
- The Pygame simulation (`standalone/pygame_sim.py`) is fully standalone and does not require other project files.

## Customization

- **Object Color Detection:** Adjust the HSV color range in `object_tracker.py` for different colored objects.
- **Pinch Threshold:** Modify the `threshold` parameter in `hand_gesture.py` or `pygame_sim.py` for sensitivity.

## License

## Acknowledgements

- [MediaPipe](https://mediapipe.dev/) for real-time hand tracking.
- [OpenCV](https://opencv.org/) for image processing.
- [Pygame](https://www.pygame.org/) for the standalone simulation interface.
