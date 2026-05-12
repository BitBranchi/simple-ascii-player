"""
ASCII Video Player 🎬
A simple script that converts video frames into ASCII art in the terminal.
Uses OpenCV for video processing and NumPy for array manipulation.

Casual project :D
"""

import cv2 as cv
import numpy as np

# Getting target file this could be file in the same folder or path to file
name = str(input("[i] Input video path : "))

# ASCII Characters
ascii_chars = " .:-=+*#%@"
num_chars = len(ascii_chars)

# Use openCV to load media
capture = cv.VideoCapture(name)

# Setting target width
try:
    target_width = int(input("[i] Target width : "))
except Exception as e:
    target_width = 80

# Main loop
while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Getting demensions of frame
    h, w, _ = frame.shape

    # Calculating target height from aspect ratio of frame
    aspect_ratio = h / w
    target_height = int(target_width * aspect_ratio * 0.5)

    # Resize frame pixels to target size and change color, in this case is BGR2GRAY
    resized = cv.resize(frame, (target_width, target_height))
    gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

    # We'll calculate every pixels into int to pass in character index
    # 255 is maximum brightness
    char_indices = (gray / 255.0 * (num_chars - 1)).astype(int)

    output = []
    for row in char_indices:
        output.append("".join([ascii_chars[i] for i in row]))

    # Printing escape sequence for new frame
    print("\033[H" + "\n".join(output), end="")

    # Listen for key 'Q' press every frame
    if cv.waitKey(1) == ord('q'):
        break # Break out of loop

# Release
capture.release()
